## 流程
- 1.数据准备与处理 Data
- 2.模型构建
    - 构建网络层
    - 拼接网络层
- 3.权值初始化 initialize_weights
- 4.损失函数 Loss function
- 5.优化器 Optimizer
- 6.迭代步骤
    - 1.forward
    - 2.compute loss
    - 3.backward
    - 4.update parameters
    - 5.clear gradient

### 1. 数据载体张量与线性回归
- ![1](pics/chp1.png)

### 2. 动态图、自动求导与逻辑回归
- ![2](pics/chp2.png)
- 区分静态图和动态图
- 自动求导机制`torch.autograd.backward()`和`torch.autograd.grad()`
    - 梯度手动清零
    - 叶子节点不能进行原位`in-place`操作
    - 依赖叶子节点的节点默认进行求梯度操作
    
### 3. 数据读取机制与图像预处理模块
- ![3](pics/chp3.png)

### 4. Module和Containers源码解析
- ![4](pics/chp4.png)
- 模块构建机制
    - 先有一个目标网络的 `Module` 继承 `nn.Module` 这个基类
    - 然后该目标网络的 `Module` 里面又可以有很多的子模块，这些子模块同样也是继承于 `nn.Module`
    - 在这些 `Module` 的`__init__`方法中，会先通过调用父类的初始化方法进行`8`个属性的一个初始化
    - 子模块构建过程：第一步是初始化，然后被`__setattr__`这个方法通过判断 `value` 的类型将其保存到相应的属性字典里面去，然后再进行赋值给相应的成员。这样一个个的构建子模块，最终把整个大的 `Module` 构建完毕
- `nn.Module`
    - `8`个重要属性，用于管理整个模型，以有序字典形式存储
        - `_parameters`：存储管理属于 `nn.Parameter` 类的属性，例如权值，偏置这些参数
        - `_modules`: 存储管理 `nn.Module` 类， 比如 LeNet 中，会构建子模块，卷积层，池化层，就会存储在 `modules` 中
        - `_buffers`: 存储管理缓冲属性，如 `BN` 层中的 `running_mean`，`std` 等都会存在这里面
        - `***_hooks`: 5个钩子函数
    - 一个 `module` 可以包含多个子 `module`(LeNet 包含卷积层，池化层，全连接层)
    - 一个 `module` 相当于一个运算， 必须实现 `forward()` 函数(从计算图的角度去理解)
    - 每个 `module` 都有 `8` 个字典管理它的属性(最常用的就是`_parameters`，`_modules` )

### 5. `nn`模块中的网络层
- ![5](pics/chp5.png)
- 卷积尺寸计算公式
    - ![5。1](pics/chp5-1.png)

### 6. 初始化与损失函数
- ![6](pics/chp6.png)
- Xavier权重初始化，有利于缓解带有sigmoid，tanh的这样的饱和激活函数的神经网络的梯度消失和爆炸现象，不过不适用于`Relu`激活函数
- 损失函数
    - ![6.1](pics/chp6.1.png)
    - 交叉熵
        - 信息熵（自信息）
            - 事件发生概率的对数再取反，概率越大，自信息越少
        - 相对熵（KL散度）
            - 衡量两个分布之间的差异（不是距离函数，因为不满足距离的三个性质之一：对称性）
        - 交叉熵
            - 交叉熵 = 信息熵 + 相对熵 （相对熵 = 交叉熵 - 信息熵）
            - ![证明过程](pics/chp6.2.png)
            
### 7. 优化器源码解析和学习率调整策略
- ![7](pics/chp7.png)

### 8. Tensorboard 可视化与 Hook 机制
- ![8](pics/chp8.png)

### 9. 正则化与标准化
- ![9](pics/chp9.png)

> Reference

[阿泽的学习笔记](https://mp.weixin.qq.com/mp/homepage?__biz=MzIwMDIzNDI2Ng==&hid=10&sn=25d0262fcb130258ed1a516f298c7ee4&scene=18#wechat_redirect)