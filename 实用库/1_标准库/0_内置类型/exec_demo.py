"""
  @Author       : liujianhan
  @Date         : 21/2/4 15:52
  @Project      : DailyTinyImprovement
  @FileName     : exec_demo.py
  @Description  : Placeholder
"""

if __name__ == '__main__':
    s = 'print("hello world")'
    t = """for i in range(5):
        print(f"iter time: {i}")
    """
    exec(s)
    exec(t)
