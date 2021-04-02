"""
  @Author       : liujianhan
  @Date         : 21/3/31 17:59
  @Project      : DailyTinyImprovement
  @FileName     : 6.1_initialize_weights.py
  @Description  : Placeholder
"""
import numpy as np
import torch
from torch import nn


class MLP(nn.Module):
    def __init__(self, neural_num, layers):
        super(MLP, self).__init__()
        self.linear = nn.ModuleList([nn.Linear(neural_num, neural_num, bias=False) for _ in range(layers)])
        self.neural_num = neural_num

    def forward(self, x):
        for i, linear in enumerate(self.linear):
            x = linear(x)
            # x = torch.tanh(x)
            x = torch.relu(x)

            print(f"layer: {i}, std: {x.std()}")
            if torch.isnan(x.std()):
                print(f"output is nan in {i} layers.")
                break
        return x

    def initialize(self):
        for m in self.modules():
            # 初始化的避免梯度爆炸和消失的指导原则：方差一致性原则
            if isinstance(m, nn.Linear):
                # 1.梯度爆炸
                # nn.init.normal_(m.weight.data)
                # 2.梯度消失
                # nn.init.normal_(m.weight.data, std=np.sqrt(1 / self.neural_num))
                # 3.适合激活函数为饱和函数（tanh,sigmoid)的初始化
                # tanh_gain = nn.init.calculate_gain('tanh')  # 计算激活函数的方差变化尺度
                # nn.init.xavier_normal_(m.weight.data, gain=tanh_gain)
                # 4.适合ReLU激活函数及变种
                nn.init.kaiming_normal_(m.weight.data)


if __name__ == '__main__':
    layer_num = 100
    neural_num = 256
    batch_size = 16
    net = MLP(neural_num, layer_num)
    net.initialize()

    inputs = torch.randn((batch_size, neural_num))
    outputs = net(inputs)

    print(outputs)
