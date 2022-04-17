# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow import keras
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

if __name__ == '__main__':
    x = tf.constant([[5, 2], [1, 3]])
    print(x)
    a = tf.random.normal(shape=(2, 2))
    b = tf.random.normal(shape=(2, 2))
    with tf.GradientTape() as tape:
        # 常量的导数需要手动watch
        tape.watch(a)
        c = tf.sqrt(tf.square(a) + tf.square(b))
        dc_da = tape.gradient(c, a)
        print(dc_da)

    a = tf.random.uniform(shape=(2, 2), minval=0, maxval=10, dtype='float32')
    b = tf.random.uniform(shape=(2, 2), minval=0, maxval=10, dtype='float32')
    print(a, b)
    a = tf.Variable(a)
    print(a)
    with tf.GradientTape() as tape:
        # 变量的导数自动watch
        c = tf.square(a) + tf.square(b)
        dc_da = tape.gradient(c, a)
        print(dc_da)

    # 多次微分
    with tf.GradientTape() as outer_tape:
        with tf.GradientTape() as tape:
            c = tf.square(a) + tf.square(b)
            dc_da = tape.gradient(c, a)
        d2c_da2 = outer_tape.gradient(dc_da, a)
        print(d2c_da2)
