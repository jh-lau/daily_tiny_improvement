"""
  @Author       : liujianhan
  @Date         : 21/4/2 16:40
  @Project      : DailyTinyImprovement
  @FileName     : 7.2_state_dict.py
  @Description  : Placeholder
"""
import torch
import os
from torch import optim

BASE_DIR = 'models'

if __name__ == '__main__':
    weight = torch.randn((2, 2), requires_grad=True)
    weight.grad = torch.ones((2, 2))
    optimizer = optim.SGD([weight], lr=.1, momentum=.8)
    print(f"State before step: \n {optimizer.state_dict()}")
    reloading = 1
    if reloading:
        state_dict = torch.load(os.path.join(BASE_DIR, 'optimizer_state_dict.pkl'))
        print(f"state dict from checkpoint: {state_dict}")
        optimizer.load_state_dict(state_dict)
        print(f"State after load state from checkpoint: \n {optimizer.state_dict()}")
    else:
        for _ in range(10):
            optimizer.step()
        print(f"State after 10 steps: \n {optimizer.state_dict()}")
        torch.save(optimizer.state_dict(), os.path.join(BASE_DIR, 'optimizer_state_dict.pkl'))