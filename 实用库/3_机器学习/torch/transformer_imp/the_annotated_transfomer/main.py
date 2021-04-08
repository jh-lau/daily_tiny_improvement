"""
  @Author       : liujianhan
  @Date         : 21/4/7 11:40
  @Project      : DailyTinyImprovement
  @FileName     : main.py
  @Description  : Placeholder
"""
import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
import math, copy, time
from src.transformer import subsequent_mask
from torch.autograd import Variable
import matplotlib.pyplot as plt
import seaborn
seaborn.set_context(context='talk')


if __name__ == '__main__':
    plt.figure(figsize=(5, 5))
    plt.imshow(subsequent_mask(20)[0])
    plt.show()