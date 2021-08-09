"""
  @Author       : liujianhan
  @Date         : 21/7/30 21:09
  @Project      : DailyTinyImprovement
  @FileName     : custom_train_loop_from_scratch.py
  @Description  : 自定义训练过程
"""
import time

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import backend as K


# 自定义损失函数2
class CustomMSE(keras.losses.Loss):
    def __init__(self, regularization_factor=0.1, name="custom_mse"):
        super().__init__(name=name)
        self.regularization_factor = regularization_factor

    def call(self, y_true, y_pred):
        mse = tf.math.reduce_mean(tf.square(y_true - y_pred))
        reg = tf.math.reduce_mean(tf.square(0.5 - y_pred))
        return mse + reg * self.regularization_factor


class MyModel(keras.Model):
    def train_step(self, data):
        if len(data) == 3:
            x, y, sample_weight = data
        else:
            sample_weight = None
            x, y = data
        with tf.GradientTape() as tape:
            y_pred = self(x, training=True)
            loss = self.compiled_loss(y,
                                      y_pred,
                                      sample_weight=sample_weight,
                                      regularization_losses=self.losses)
        gradients = tape.gradient(loss, self.trainable_variables)
        self.optimizer.apply_gradients(zip(gradients, self.trainable_variables))
        self.compiled_metrics.update_state(y, y_pred)
        return {m.name: m.result() for m in self.metrics}

    def test_step(self, data):
        x, y = data
        y_pred = self(x, training=True)
        self.compiled_loss(y, y_pred, regularization_losses=self.losses)
        self.compiled_metrics.update_state(y, y_pred)
        return {m.name: m.result() for m in self.metrics}


loss_tracker = keras.metrics.Mean(name='loss')
mae_metric = keras.metrics.MeanAbsoluteError(name='mae')


class MyModel2(keras.Model):
    def train_step(self, data):
        x, y = data
        with tf.GradientTape() as tape:
            y_pred = self(x, training=True)
            loss = keras.losses.mean_squared_error(y, y_pred)

        trainable_vars = self.trainable_variables
        gradients = tape.gradient(loss, trainable_vars)

        self.optimizer.apply_gradients(zip(gradients, trainable_vars))

        loss_tracker.update_state(loss)
        mae_metric.update_state(y, y_pred)
        return {'loss': loss_tracker.result(), 'mae': mae_metric.result()}

    @property
    def metrics(self):
        return [loss_tracker, mae_metric]


if __name__ == '__main__':
    inputs = keras.Input(shape=(32, ))
    outputs = keras.layers.Dense(1)(inputs)
    model = MyModel(inputs, outputs)
    model2 = MyModel2(inputs, outputs)
    model.compile(optimizer='adam', loss=CustomMSE(), metrics=['mae'])
    model2.compile(optimizer='adam')

    x = np.random.random((1000, 32))
    y = np.random.random((1000, 1))
    sw = np.random.random((1000, 1))
    model.fit(x, y, sample_weight=sw, epochs=3)
    # model.evaluate(x, y)
    # model2.fit(x, y, epochs=3)
