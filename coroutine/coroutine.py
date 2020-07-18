"""
  @Author       : Liujianhan
  @Date         : 20/7/18 23:18
  @FileName     : coroutine.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """


def gen():
    # 产出，且接收值
    yield 12
    html = yield 'www.baidu.com'
    print('inside', html)
    yield 1
    yield 2
    yield 3
    return 'django'


if __name__ == '__main__':
    s = gen()
    # 首次启动生成器，可通过next，或者用send传入None值
    res = s.send(None)
    print(res)
    html = next(s)
    # s.close()
    print('ouside', html)
    print(s.send('www.hello.com'))
    print(next(s))
    print(next(s))
    # 传值给生成器，并重新启动生成器，得到生成器的下一个值
    # print(s.send('www.google.com'))
    # print(next(s))
    # print(next(s))
    # print(next(s))
