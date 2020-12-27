"""
  @Author       : liujianhan
  @Date         : 2020/12/26 15:53
  @Project      : DailyTinyImprovement
  @FileName     : simplenamespace_demo.py
  @Description  : Placeholder
"""
from types import SimpleNamespace as SN
from collections import abc


def dot_dict(info):
    if isinstance(info, abc.Mapping):
        res = SN(**info)
        for k, v in info.items():
            if isinstance(v, abc.Mapping):
                res.__dict__[k] = dot_dict(v)

        return res


if __name__ == '__main__':
    s = SN()
    s.data = {}
    s.name = 'liujianhan'
    s.age = 199
    t = {'name': 'joey', 'gender': 'male', '1': 12}
    t1 = SN(**t)
    # 嵌套字典
    r = {'name': 'ross'}
    r1 = {'gender': 'male', 'age': 12, 'another_name': SN(**r)}
    r2 = SN(**r1)
    print(r2.gender, r2.age, r2.another_name.name)
    # 封装方法
    d = {'name': 'gary', 'gender': 'male', 'age': 40,
         'child': {'name': 'josy', 'age': 123, 'child': {'name': 'chand', 'age': 2}}}
    res = dot_dict(d)
    print(res)
    print(res.name, res.gender, res.age)
    print(res.child.name, res.child.age, res.child.child)
    print(res.child.child.name, res.child.child.age)
