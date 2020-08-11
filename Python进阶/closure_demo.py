"""
  @Author       : Liujianhan
  @Date         : 20/8/11 21:29
  @FileName     : closure_demo.py
  @ProjectName  : DailyTinyImprovement
  @Description  : 闭包
  1. 嵌套函数
  2. 闭包引用外部变量
  3. 闭包返回
 """


def outside(x):
    def closure(y):
        result = (x - y) / (x + y)
        return result

    return closure


if __name__ == '__main__':
    s = outside(10)
    print(s(5))
