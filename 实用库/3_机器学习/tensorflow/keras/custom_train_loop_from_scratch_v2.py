"""
  @Author       : liujianhan
  @Date         : 21/7/30 21:09
  @Project      : DailyTinyImprovement
  @FileName     : custom_train_loop_from_scratch.py
  @Description  : Placeholder
"""
import time

import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras import backend as K


# 自定义损失函数1, tf version
def my_crossentropy(y_true, y_pred, e=0.1):
    loss1 = tf.losses.sparse_categorical_crossentropy(y_true, y_pred, from_logits=True)
    y_pred_label = tf.argmax(y_pred, axis=-1)
    weight = tf.cast((y_pred_label - y_true), tf.float32)
    weight = tf.abs(weight) + 1.
    loss1 *= weight

    # loss1 = K.sum(loss1) / 64
    loss1 = tf.math.reduce_mean(loss1)
    return loss1


def my_crossentropy_keras_version(y_true, y_pred, e=0.1):
    loss1 = K.sparse_categorical_crossentropy(y_true, y_pred, from_logits=True)
    y_pred_label = K.argmax(y_pred, axis=-1)
    weight = K.cast((y_pred_label - y_true), tf.float32)
    weight = K.abs(weight) + 1.
    loss1 *= weight

    # loss1 = K.sum(loss1) / 64
    loss1 = tf.math.reduce_mean(loss1)
    return loss1


@tf.function
def train_step(x, y):
    with tf.GradientTape() as tape:
        logits = model(x, training=True)
        loss_value = loss_fn(y, logits)
    grads = tape.gradient(loss_value, model.trainable_weights)
    optimizer.apply_gradients(zip(grads, model.trainable_weights))
    train_acc_metric.update_state(y, logits)
    return loss_value


@tf.function
def test_step(x, y):
    logits = model(x, training=False)
    val_acc_metric.update_state(y, logits)


if __name__ == '__main__':
    inputs = keras.Input(shape=(784,), name='digits')
    x1 = layers.Dense(64, activation='relu')(inputs)
    x2 = layers.Dense(64, activation='relu')(x1)
    outputs = layers.Dense(10, name='predictions')(x2)
    model = keras.Model(inputs, outputs)

    optimizer = keras.optimizers.SGD(learning_rate=1e-3)
    # loss_fn = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
    loss_fn = my_crossentropy
    train_acc_metric = keras.metrics.SparseCategoricalAccuracy()
    val_acc_metric = keras.metrics.SparseCategoricalAccuracy()

    batch_size = 64
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train = np.reshape(x_train, (-1, 784))
    x_test = np.reshape(x_test, (-1, 784))
    y_train = tf.cast(y_train, tf.int64)
    y_test = tf.cast(y_test, tf.int64)
    train_dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    train_dataset = train_dataset.shuffle(buffer_size=1924).batch(batch_size)

    x_val = x_train[-10000:]
    y_val = y_train[-10000:]
    x_train = x_train[:-10000]
    y_train = y_train[:-10000]
    val_dataset = tf.data.Dataset.from_tensor_slices((x_val, y_val))
    val_dataset = val_dataset.batch(64)

    epochs = 2
    for epoch in range(epochs):
        print(f"\nStart of epoch {epoch}")
        start_time = time.time()
        for step, (x_batch_train, y_batch_train) in enumerate(train_dataset):
            loss_value = train_step(x_batch_train, y_batch_train)

            if step % 200 == 0:
                print(
                    f"Training loss (for one batch) at step {step}: {float(loss_value): .4f}"
                )
                print(f"Seen so far: {(step + 1) * 64} samples")
        train_acc = train_acc_metric.result()
        print(f"Training acc over epoch: {train_acc: .4f}")
        train_acc_metric.reset_state()

        for x_bach_val, y_bach_val in val_dataset:
            test_step(x_bach_val, y_bach_val)
        val_acc = val_acc_metric.result()
        val_acc_metric.reset_states()
        print(f"Validation acc: {val_acc: .4f}")
        print(f"Time taken: {time.time() - start_time: .2f}")