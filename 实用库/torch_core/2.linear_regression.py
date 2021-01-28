"""
  @Author       : liujianhan
  @Date         : 2021/1/27 14:39
  @Project      : DailyTinyImprovement
  @FileName     : 2.linear_regression.py
  @Description  : Placeholder
"""
import torch as th


if __name__ == '__main__':
    x = th.rand(20, 1) * 10
    y = 2 * x + (5 + th.randn(20, 1))

    lr = 1e-3
    w = th.randn((1,), requires_grad=True)
    b = th.zeros((1,), requires_grad=True)

    for i in range(100):
        wx = th.mul(w, x)
        y_pred = th.add(wx, b)

        loss = (.5 * (y - y_pred) ** 2).mean()

        loss.backward()

        b.data.sub_(lr * b.grad)
        w.data.sub_(lr * w.grad)

        w.grad.data.zero_()
        b.grad.data.zero_()

        print(w.data, b.data)