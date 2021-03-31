"""
  @Author       : liujianhan
  @Date         : 21/2/23 11:58
  @Project      : DailyTinyImprovement
  @FileName     : ping3_demo.py
  @Description  : Placeholder
"""
from ping3 import ping


if __name__ == '__main__':
    url = '192.168.3.103'
    # url = '192.168.1.200'
    # url = 'www.baidu.com'
    count = 0
    for i in range(1000):
        second = ping(url, timeout=1.5, unit='ms')
        if second is None:
            count += 1
            print(f"当前超时次数 {count}: 第 {i} 次尝试超时")
    print(f"共超时次数：{count}")