"""
  @Author       : liujianhan
  @Date         : 21/3/31 17:59
  @Project      : DailyTinyImprovement
  @FileName     : 6.1_initialize_and_loss_function.py
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
            x = torch.tanh(x)

            print(f"layer: {i}, std: {x.std()}")
            if torch.isnan(x.std()):
                print(f"output is nan in {i} layers.")
                break
        return x

    def initialize(self):
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.normal_(m.weight.data, std=np.sqrt(1 / self.neural_num))


if __name__ == '__main__':
    layer_num = 100
    neural_num = 256
    batch_size = 16
    net = MLP(neural_num, layer_num)
    net.initialize()

    inputs = torch.randn((batch_size, neural_num))
    outputs = net(inputs)

    print(outputs)
