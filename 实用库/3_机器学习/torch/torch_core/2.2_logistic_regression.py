"""
  @Author       : liujianhan
  @Date         : 21/3/30 13:59
  @Project      : DailyTinyImprovement
  @FileName     : 2.2_logistic_regression.py
  @Description  : Placeholder
"""
import torch as t
from matplotlib import pyplot as plt
import numpy as np


class LR(t.nn.Module):
    def __init__(self):
        super(LR, self).__init__()
        self.features = t.nn.Linear(2, 1)
        self.sigmoid = t.nn.Sigmoid()

    def forward(self, x):
        x = self.features(x)
        x = self.sigmoid(x)
        return x


if __name__ == '__main__':
    t.manual_seed(1)
    sample_nums = 100
    mean_value = 1.7
    bias = 1

    n_data = t.ones(sample_nums, 2)
    x0 = t.normal(mean_value * n_data, 1) + bias
    y0 = t.zeros(sample_nums)
    x1 = t.normal(-mean_value * n_data, 1) + bias
    y1 = t.ones(sample_nums)

    train_x = t.cat([x0, x1], 0)
    train_y = t.cat([y0, y1], 0)
    # Model
    lr_net1 = LR()
    # lr_net2 = t.nn.Sequential(
    #     t.nn.Linear(2, 1),
    #     t.nn.Sigmoid()
    # )
    # Loss function
    loss_fn = t.nn.BCELoss()
    lr = .01
    # Optimizer
    optimizer = t.optim.SGD(lr_net1.parameters(), lr=lr, momentum=.9)
    iterations = 1000
    for it in range(iterations):
        # 1-forward
        y_pred = lr_net1(train_x)
        # y_pred = lr_net2(train_x)
        # 2-loss
        loss = loss_fn(y_pred.squeeze(), train_y)
        # 3-backward
        loss.backward()
        # 4-update parameters
        optimizer.step()
        # 5-clean grad
        optimizer.zero_grad()
        if it % 20 == 0:
            print(f"Start {it}th iteration learning...")
            mask = y_pred.ge(.5).float().squeeze()
            correct = (mask == train_y).sum()
            acc = correct.item() / train_y.size(0)

            plt.scatter(x0.data.numpy()[:, 0], x0.data.numpy()[:, 1], c='r', label='class 0')
            plt.scatter(x1.data.numpy()[:, 0], x1.data.numpy()[:, 1], c='b', label='class 1')

            w0, w1 = lr_net1.features.weight[0]
            w0, w1 = float(w0.item()), float(w1.item())
            plot_b = float(lr_net1.features.bias[0].item())
            plot_x = np.arange(-6, 6, .1)
            plot_y = (-w0 * plot_x - plot_b) / w1
            plt.xlim(-5, 7)
            plt.ylim(-7, 7)
            plt.plot(plot_x, plot_y)
            plt.text(-5, 5, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
            plt.title(
                "Iteration: {}\nw0:{:.2f} w1:{:.2f} b: {:.2f} accuracy:{:.2%}".format(it, w0, w1, plot_b, acc))
            plt.legend()

            plt.show()
            plt.pause(0.5)

            if acc > 0.99:
                break
