"""
  @Author       : Liujianhan
  @Date         : 20/7/18 23:45
  @FileName     : demo2_throw_test.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """


def gen():
    try:
        yield 'hello.com'
    except Exception as e:
        print(e)
    yield 1
    yield 2
    yield 3
    return 'django'


if __name__ == '__main__':
    s = gen()
    print(next(s))
    print(s.throw(Exception, 'something wrong here'))
    print(next(s))
