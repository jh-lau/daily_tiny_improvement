"""
  @Author       : liujianhan
  @Date         : 21/4/2 10:17
  @Project      : DailyTinyImprovement
  @FileName     : 6.2_loss_function.py
  @Description  : Placeholder
"""
import torch
from torch import nn
import numpy as np


if __name__ == '__main__':
    flag = 1
    # fake data
    inputs = torch.tensor([[1, 2], [1, 3], [1, 3], [1, 3]], dtype=torch.float)  # model outputs
    target = torch.tensor([0, 1, 1, 0], dtype=torch.long)  # ground truth
    if flag == 1:
        m = nn.LogSoftmax(dim=1)
        print(-m(inputs))
        loss = nn.NLLLoss(reduction='none')
        outputs = loss(m(inputs), target)
        print(outputs)
    elif flag == 2:
        m = np.log(nn.Softmax(dim=1)(inputs))  # 等于nn.LogSoftmax(dim=1)
        print(-m)
    else:
        weights = torch.tensor([1, 2], dtype=torch.float)
        weight_flag = 1
        weight = weights if weight_flag else None
        loss_f_none = nn.CrossEntropyLoss(weight=weight, reduction='none')
        loss_f_sum = nn.CrossEntropyLoss(weight=weight, reduction='sum')
        loss_f_mean = nn.CrossEntropyLoss(weight=weight, reduction='mean')

        loss_none = loss_f_none(inputs, target)
        loss_sum = loss_f_sum(inputs, target)
        loss_mean = loss_f_mean(inputs, target)

        print(f'Cross Entropy Loss:\n {loss_none, loss_sum, loss_mean}')
