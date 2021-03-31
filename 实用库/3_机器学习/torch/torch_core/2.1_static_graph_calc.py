"""
  @Author       : liujianhan
  @Date         : 21/3/30 10:55
  @Project      : DailyTinyImprovement
  @FileName     : 2.1_static_graph_calc.py
  @Description  : Placeholder
"""
import torch as t

if __name__ == '__main__':
    flag = 0
    if flag == 0:
        w = t.tensor([1.], requires_grad=True)
        x = t.tensor([2.], requires_grad=True)

        a = t.add(w, x)
        a.retain_grad()
        b = t.add(w, 1)
        y = t.mul(a, b)
        y1 = t.add(a, b)
        # print(y)
        loss = t.cat([y, y1], dim=0)  # 多个loss，需要分配权重

        # loss权重分配
        # loss.backward(gradient=t.tensor([1., 1.]))
        loss.backward(gradient=t.tensor([1., 2.]))
        print(w.grad)
        print("is_leaf:\n", w.is_leaf, x.is_leaf, a.is_leaf, b.is_leaf, y.is_leaf)
        print("gradient:\n", w.grad, x.grad, a.grad, b.grad, y.grad)
        print("grad_fn:\n", w.grad_fn, x.grad_fn, a.grad_fn, b.grad_fn, y.grad_fn)
        print(f"requires_grad:\n{a.requires_grad}, {b.requires_grad}, {y.requires_grad}")
    elif flag == 1:
        x = t.tensor([3.], requires_grad=True)
        y = t.pow(x, 2)
        grad_1 = t.autograd.grad(y, x, create_graph=True)
        print(grad_1)
        grad_2 = t.autograd.grad(grad_1[0], x)
        print(grad_2)
    elif flag == 2:
        x1 = t.tensor(1., requires_grad=True)
        x2 = t.tensor(2., requires_grad=True)
        y1 = x1 * x2
        y2 = x1 + x2
        y1x1_grad, y1x2_grad = t.autograd.grad(outputs=y1, inputs=[x1, x2], retain_graph=True)
        print(y1x1_grad, y1x2_grad)
        y12x1_grad, y12x2_grad = t.autograd.grad(outputs=[y1, y2], inputs=[x1, x2])
        print(y12x1_grad, y12x2_grad)
    elif flag == 3:
        w = t.tensor([1.], requires_grad=True)
        x = t.tensor([2.], requires_grad=True)
        for i in range(4):
            a = t.add(w, x)
            b = t.add(w, 1)
            y = t.mul(a, b)
            y.backward()
            print(w.grad)
            w.grad.zero_()  # 注意梯度清零
    else:
        import tensorflow as tf

        w = tf.constant(1.)
        x = tf.constant(2.)
        a = tf.add(w, x)
        b = tf.add(w, 1)
        y = tf.multiply(a, b)
        print(y)
        with tf.compat.v1.Session() as sess:
            print(sess.run(y))
