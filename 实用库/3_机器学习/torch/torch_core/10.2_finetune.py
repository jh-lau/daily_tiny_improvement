"""
  @Author       : liujianhan
  @Date         : 21/4/6 16:22
  @Project      : DailyTinyImprovement
  @FileName     : 10.2_finetune.py
  @Description  : Placeholder
"""
import torch
from torch import nn, optim
from torchvision import models

if __name__ == '__main__':
    classes = 2
    resnet18 = models.resnet18()
    state_dict = torch.load('./models/resnet18-5c106cde.pth')
    resnet18.load_state_dict(state_dict)
    flag = 0
    if flag == 0:
        # 方式1
        for param in resnet18.parameters():
            param.requires_grad = False  # 冻结层参数
        num_features = resnet18.fc.in_features
        resnet18.fc = nn.Linear(num_features, classes)  # 修改最后的输出层
    elif flag == 1:
        # 方式2：将学习率设置为0
        fc_params_id = {id(param) for param in resnet18.fc.parameters()}
        base_params = {id(param) for param in resnet18.parameters()} - fc_params_id
        optimizer = optim.SGD([
            {'params': base_params, 'lr': 0},
            {'params': resnet18.fc.parameters(), 'lr': .005}
        ], momentum=.9)
        scheduler = optim.lr_scheduler.StepLR(optimizer, gamma=.1)
        # do training
    print(resnet18)
