"""
  @Author       : liujianhan
  @Date         : 2021/7/5 9:14
  @Project      : DailyTinyImprovement
  @FileName     : plot_model.py
  @Description  : Placeholder
"""
import tensorflow as tf

if __name__ == '__main__':
    inputs = tf.keras.Input(shape=(100,), dtype='int32', name='input')
    x = tf.keras.layers.Embedding(
        output_dim=512, input_dim=10000, input_length=100)(inputs)
    x = tf.keras.layers.LSTM(32)(x)
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    x = tf.keras.layers.Dense(64, activation='relu')(x)
    output = tf.keras.layers.Dense(1, activation='sigmoid', name='output')(x)
    model = tf.keras.Model(inputs=[inputs], outputs=[output])
    dot_img_file = 'model_1.png'
    tf.keras.utils.plot_model(model, to_file=dot_img_file, show_shapes=True)
