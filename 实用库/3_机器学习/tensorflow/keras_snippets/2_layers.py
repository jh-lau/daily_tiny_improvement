# -*- coding: utf-8 -*-

import tensorflow as tf
from tensorflow import keras


class Linear(keras.layers.Layer):
    """y = w.x + b"""

    def __init__(self, units=32, input_dim=32):
        super().__init__()
        w_init = tf.random_normal_initializer()
        self.w = tf.Variable(
            initial_value=w_init(shape=(input_dim, units), dtype='float32'),
            trainable=True
        )
        b_init = tf.zeros_initializer()
        self.b = tf.Variable(
            initial_value=b_init(shape=(units,), dtype='float32'),
            trainable=True
        )

    def call(self, inputs):
        print(inputs)
        return tf.matmul(inputs, self.w) + self.b


if __name__ == '__main__':
    linear_layer = Linear(4, 2)
    y = linear_layer(tf.ones((2, 2)))
    print(linear_layer.weights)
    print(y)
