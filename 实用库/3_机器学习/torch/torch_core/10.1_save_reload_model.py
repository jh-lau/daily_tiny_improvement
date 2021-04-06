"""
  @Author       : liujianhan
  @Date         : 21/4/6 15:28
  @Project      : DailyTinyImprovement
  @FileName     : 10.1_save_reload_model.py
  @Description  : Placeholder
"""
import torch
from torch import nn, optim


class LeNetSequential(nn.Module):
    def __init__(self, classes):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 6, 5),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Conv2d(6, 16, 5),
            nn.ReLU(),
            nn.MaxPool2d(2, 2)
        )
        self.classifier = nn.Sequential(
            nn.Linear(16 * 5 * 5, 120),
            nn.ReLU(),
            nn.Linear(120, 84),
            nn.ReLU(),
            nn.Linear(84, classes)
        )

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size()[0], -1)
        x = self.classifier(x)

        return x

    def initialize(self):
        for p in self.parameters():
            p.data.fill_(20210404)


if __name__ == '__main__':
    path_model = './models/model_10.pkl'
    path_state_dict = './models/model_10_static_dict.pkl'
    path_checkpoint = './models/checkpoint_10.pkl'
    flag = 3
    if flag == 0:
        net = LeNetSequential(2021)
        print(f"Before training: {net.features[0].weight[0, ...]}")
        net.initialize()
        print(f"After training: {net.features[0].weight[0, ...]}")
        # 保存方式1：保存整个模型
        torch.save(net, path_model)
        # 方式2：保存模型参数
        torch.save(net.state_dict(), path_state_dict)
    elif flag == 1:
        # 从整个模型中恢复
        net_load = torch.load(path_model)
        print(net_load)
    elif flag == 2:
        # 从模型参数中恢复（推荐）
        net_new = LeNetSequential(2021)
        state_dict_load = torch.load(path_state_dict)
        net_new.load_state_dict(state_dict_load)
        print(net_new)
    elif flag == 3:
        save_interval = 5
        net_new = LeNetSequential(2021)
        optimizer = optim.SGD(net_new.parameters(), lr=.0005, momentum=.8)
        scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=.1)

        for epoch in range(100):
            # do training
            # save model
            if epoch % save_interval == 0:
                checkpoint = {
                    'model_state_dict': net_new.state_dict(),
                    'optimizer_state_dict': optimizer.state_dict(),
                    'epoch': epoch
                }
                torch.save(checkpoint, path_checkpoint)
            # bug occurs, training stops
            # reloading from checkpoint
            checkpoint_reload = torch.load(path_checkpoint)
            net_new.load_state_dict(checkpoint_reload['model_state_dict'])
            optimizer.load_state_dict(checkpoint_reload['optimizer_state_dict'])
            start_epoch = checkpoint_reload['epoch']
            scheduler.last_epoch = start_epoch
            # continue training
