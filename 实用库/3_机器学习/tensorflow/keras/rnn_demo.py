"""
  @Author       : liujianhan
  @Date         : 21/7/7 21:10
  @Project      : DailyTinyImprovement
  @FileName     : rnn_demo.py
  @Description  : Placeholder
"""
import tensorflow as tf

if __name__ == '__main__':
    inputs = tf.random.normal([32, 10, 8])
    lstm = tf.keras.layers.LSTM(4)
    output = lstm(inputs)
    print(output.shape)
    lstm = tf.keras.layers.LSTM(4, return_sequences=True, return_state=True)
    whole_seq_output, final_memory_state, final_carry_state = lstm(inputs)
    print(whole_seq_output.shape)
    print(final_memory_state.shape)
    print(final_carry_state.shape)
