"""
  @Author       : liujianhan
  @Date         : 21/1/21 23:09
  @Project      : DailyTinyImprovement
  @FileName     : 1.1_tensor.py
  @Description  : https://mp.weixin.qq.com/s?__biz=MzIwMDIzNDI2Ng==&mid=2247486164&idx=1&sn=b26c0ebcf9b494c4acaef41a4292c5e4&scene=19#wechat_redirect
"""
import torch as th
import numpy as np

if __name__ == '__main__':
    arr = np.ones((3, 3))
    print(arr.dtype)
    print(th.cuda.is_available())
    # 与arr共享内存
    t = th.tensor(arr, device='cpu')

    # 张量属性
    print(t.data)
    print(t.dtype)
    print(t.shape)
    print(t.device)
    print(t.requires_grad)
    print(t.grad)
    print(t.grad_fn)
    print(t.is_leaf)

    # 创建张量
    out_t = th.tensor([1])
    t = th.zeros((3, 3), out=out_t)  # out参数，将该值也赋值给out_t
    print(out_t, '\n', t)
    print(id(t), id(out_t))
    print(th.zeros_like(out_t))
    print(th.full_like(t, 10))
    print(th.full((3, 3,), 2))
    print(th.arange(2, 10, 2))  # 注意和下面的区别，一个是步长step，下面是数列长度steps
    print(th.linspace(2, 10, 6))  # steps
    print(th.logspace(2, 10, 8))
    print(th.eye(3, 5))

    # 概率分布
    print(th.normal(0, 1, (4,)))  # 正态分布
    print(th.randn((3, 2)))  # 标准正态分布
    # print(th.randn_like(t))
    print(th.rand(t.shape))
    # print(th.rand_like())  # 均匀分布
    print(th.randint(0, 10, (3,3)))
    # print(th.randint_like(t))
