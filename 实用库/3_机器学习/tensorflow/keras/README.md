1. Input层的作用
    - 构建模型时，确定tensor的形状，以便调用summary或者plot_model在模型构建后（不需要build）即可观察模型架构
    - 带Input层的模型具有各层的初始权重，计时还没见过真实的数据
    - Input不属于模型层，tensor