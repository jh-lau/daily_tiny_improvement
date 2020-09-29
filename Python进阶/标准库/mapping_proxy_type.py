"""
  @Author       : liujianhan
  @Date         : 2020/9/29 18:59
  @Project      : DailyTinyImprovement
  @FileName     : mapping_proxy_type.py
  @Description  : 不可变的映射类型：只读，可通过修改原始映射进行修改
"""
from types import MappingProxyType

if __name__ == '__main__':
    s = dict(zip(range(4), 'abcd'))
    s['a'] = 1000
    print(s)
    new_s = MappingProxyType(s)
    # new_s['a'] = 110
    print(new_s)
    s['b'] = 101
    print(new_s)