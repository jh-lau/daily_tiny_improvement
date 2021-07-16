"""
  @Author       : liujianhan
  @Date         : 21/7/15 22:09
  @Project      : DailyTinyImprovement
  @FileName     : demo.py
  @Description  : Placeholder
"""
import tensorflow as tf
from tensorflow.keras import layers, Model
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
from tensorflow.keras.utils import plot_model

if __name__ == '__main__':
    inputs = layers.Input(shape=(), dtype=tf.string)
    vec = TextVectorization(vocabulary=[str(i) for i in range(10)])
    x = vec(inputs)
    emb = layers.Embedding(input_dim=12, output_dim=16)
    x = emb(x)
    lstm = layers.LSTM(16)
    outputs = lstm(x)
    model = Model(inputs=inputs, outputs=outputs)
    # plot_model(model, to_file='vec.png', show_shapes=True)
