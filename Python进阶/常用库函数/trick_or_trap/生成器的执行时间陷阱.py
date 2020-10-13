"""
  @Author       : liujianhan
  @Date         : 2020/7/29 下午2:03
  @Project      : DailyTinyImprovement
  @FileName     : 生成器的执行时间陷阱.py
  @Description  : 在生成器表达式中, in 子句在声明时执行, 而条件子句则是在运行时执行.
所以在运行前, array 已经被重新赋值为 [2, 8, 22], 因此对于之前的 1, 8 和 15, 只有 count(8) 的结果是大于 0 的, 所以生成器只会生成 8.
第二部分中 g1 和 g2 的输出差异则是由于变量 array_1 和 array_2 被重新赋值的方式导致的.
在第一种情况下, array_1 被绑定到新对象 [1,2,3,4,5], 因为 in 子句是在声明时被执行的， 所以它仍然引用旧对象 [1,2,3,4](并没有被销毁).
在第二种情况下, 对 array_2 的切片赋值将相同的旧对象 [1,2,3,4] 原地更新为 [1,2,3,4,5]. 因此 g2 和 array_2 仍然引用同一个对象(这个对象现在已经更新为 [1,2,3,4,5]).
"""
list1 = [1, 8, 13, 14]
g = (x for x in list1 if list1.count(x) > 0)
list1 = [2, 8, 13, 145]
print(list(g))

list2 = [1, 2, 3, 4]
g1 = (x for x in list2)
# to a new list
list2 = [2, 3, 4, 5]

list3 = [2, 3, 4, 5]
g2 = (x for x in list3)
# inplace update
list3[:] = [2, 3, 4, 5, 6]

print(list(g1))
print(list(g2))
