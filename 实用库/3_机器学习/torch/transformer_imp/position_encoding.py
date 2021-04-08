"""
  @Author       : liujianhan
  @Date         : 21/4/7 10:05
  @Project      : DailyTinyImprovement
  @FileName     : position_encoding.py
  @Description  : Placeholder
"""
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


def get_position_encoding(max_seq_len, embed_dim):
    """
    初始化位置编码
    :param max_seq_len: 序列最大长度
    :param embed_dim: 向量维度
    :return:
    """
    positional_encoding = np.array([
        [np.sin(pos / np.power(10000, 2 * i / embed_dim)) if i % 2 == 0 else
         np.cos(pos / np.power(10000, 2 * i / embed_dim))
         for i in range(embed_dim)]
        for pos in range(max_seq_len)
    ])

    return positional_encoding


if __name__ == '__main__':
    positional_encoding = get_position_encoding(4, 512)
    plt.figure(figsize=(10, 10))
    sns.heatmap(positional_encoding)
    plt.title('Sinusoidal Function')
    plt.xlabel('hidden dimension')
    plt.ylabel('sequence length')

    plt.figure(figsize=(8, 5))
    plt.plot(positional_encoding[1:, 1], label='dimiension 1')
    plt.plot(positional_encoding[1:, 2], label='dimiension 2')
    plt.plot(positional_encoding[1:, 3], label='dimiension 3')
    plt.legend()
    plt.xlabel('sequence length')
    plt.ylabel('period of positional encoding')
    print(positional_encoding.shape)
    plt.show()
