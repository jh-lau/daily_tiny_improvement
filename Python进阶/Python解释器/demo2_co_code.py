"""
  @Author       : liujianhan
  @Date         : 20/10/2 0:12
  @Project      : DailyTinyImprovement
  @FileName     : demo2_co_code.py
  @Description  : cond.__code__ 是其 code object ，cond.__code__.co_code 是其字节码
  dis每行输出含义：
    1.字节码对应的在源代码中的行号
    2.该字节码在字节码串中的第几个字节，也就是该字节码的序号
    3.字节码的人类可读的名字
    4.字节码参数
    5.字节码参数的内容提示
    dis.opname:
        JUMP_ABSOLUTE 使解释器跳转到循环开始的位置继续执行
"""
import dis


def cond():
    x = 3
    if x < 5:
        return 'yes'
    else:
        return 'no'


def loop():
    x = 1
    while x < 5:
        x += 1
    return x


def loop1():
    t = 0
    for x in range(10):
        print(x)
        t += x
    return t


def elif_cond(x):
    if x > 1:
        print('hello')
    elif isinstance(x, str):
        print('string')
    else:
        print('world')


def list_comp():
    return [s for s in range(10) if s < 4]


if __name__ == '__main__':
    print(cond.__code__.co_code)
    byte_array = list(bytearray(cond.__code__.co_code))
    print(byte_array)
    for op in byte_array[::2]:
        print(dis.opname[op])
    # print(dis.dis(cond))
    # print(dis.dis(loop))
    # print(dis.dis(loop1))
    print(dis.dis(elif_cond))
    print(dis.dis(list_comp))
