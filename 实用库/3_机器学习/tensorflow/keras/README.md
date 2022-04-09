1. Input层的作用
    - 构建模型时，确定tensor的形状，以便调用summary或者plot_model在模型构建后（不需要build）即可观察模型架构
    - 带Input层的模型具有各层的初始权重，即使还没见过真实的数据
    - Input不属于模型层，tensor 
2. Keras组网方式
    - Sequential API:方便，缺乏灵活，无法深度自定义
    - Functional API:函数式组网
    - SubModel:继承式组网
        - 最灵活的组网模式，可组建动态网络
        - 丧失函数式api方法的一些特性：无法提前检查架构输入输出、架构可被克隆等
3. build函数用处
    - 将层参数初始化放到build函数中，可以避免需要提前知道各层的参数形状，即懒加载：在层被实例化后，层调用call函数时会自动调用build函数中的权重初始化工作。
4. 自定义数据类：keras.utils.Sequence用法
    - [demo](./semantic_similarity_with_BERT.py)