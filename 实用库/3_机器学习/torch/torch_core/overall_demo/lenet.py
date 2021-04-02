"""
  @Author       : liujianhan
  @Date         : 21/3/31 14:59
  @Project      : DailyTinyImprovement
  @FileName     : lenet.py
  @Description  : Placeholder
"""
import torch.nn.functional as F
from torch import nn


class LeNet(nn.Module):
    def __init__(self, classes):
        super(LeNet, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.covn2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, classes)

    def forward(self, x):
        out = F.relu(self.conv1(x))
        out = F.max_pool2d(out, 2)
        out = F.relu(self.conv(out))
        out = F.max_pool2d(out, 2)
        out = out.view(out.size(0), -1)
        out = F.relu(self.fc1(out))
        out = F.relu(self.fc2(out))
        out = self.fc3(out)
        return out

    def initialize_weights(self):
        # todo
        for m in self.modules():
            # 初始化的避免梯度爆炸和消失的指导原则：方差一致性原则
            if isinstance(m, nn.Linear):
                nn.init.kaiming_normal_(m.weight.data)
