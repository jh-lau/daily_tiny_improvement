"""
  @Author       : liujianhan
  @Date         : 2021/1/27 14:39
  @Project      : DailyTinyImprovement
  @FileName     : 1.2_linear_regression.py
  @Description  : Placeholder
"""
import torch as th


if __name__ == '__main__':
    x = th.rand(20, 1) * 10
    w, b = 2, 5
    y = w * x + (b + th.randn(20, 1))

    lr = 1e-3
    w = th.randn((1,), requires_grad=True)
    b = th.zeros((1,), requires_grad=True)

    for i in range(100000):
        # 前向传播
        wx = th.mul(w, x)
        y_pred = th.add(wx, b)

        # 计算损失
        loss = (.5 * (y - y_pred) ** 2).mean()

        # 反向传播
        loss.backward()

        # 梯度更新
        w.data.sub_(lr * w.grad)
        b.data.sub_(lr * b.grad)

        # 梯度清零
        w.grad.data.zero_()
        b.grad.data.zero_()

        print(w.data, b.data)
