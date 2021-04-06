"""
  @Author       : liujianhan
  @Date         : 21/4/2 15:49
  @Project      : DailyTinyImprovement
  @FileName     : 7.1_optimizer.py
  @Description  : Placeholder
"""
import torch
from torch import optim

if __name__ == '__main__':
    weight = torch.randn((2, 2), requires_grad=True)
    weight.grad = torch.ones((2, 2))

    optimizer = optim.SGD([weight], lr=.1, momentum=.8)
    print(f"weight before step:\n {weight.data}")
    print(f"optimizer before step: \n {optimizer.state_dict()}")
    for _ in range(10):
        optimizer.step()  # w = w - lr * w.grad
    print(f"weight after step:\n {weight.data}")
    print(f"optimizer after step: \n {optimizer.state_dict()} \n")

    print(f"weight in optimizer: {id(optimizer.param_groups[0]['params'][0])}\n"
          f"weight in weight: {id(weight)}")

    print(f"weight.grad is {weight.grad}\n")
    optimizer.zero_grad()
    print(f"weight.grad after clear is {weight.grad}\n")
