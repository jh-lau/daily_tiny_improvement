"""
  @Author       : liujianhan
  @Date         : 2021/5/7 15:53
  @Project      : DailyTinyImprovement
  @FileName     : json_hook_function.py
  @Description  : json实现点号访问多层级字典数据
"""
import json
from types import SimpleNamespace as SN
from argparse import Namespace as N

if __name__ == '__main__':
    d = {'name': 'gary', 'gender': 'male', 'age': 40,
         'child': [{'name': 'josy', 'age': 123, 'child': {'name': 'chand', 'age': 2}},
                   {'name': 'josy', 'age': 123, 'child': {'name': 'chand', 'age': 2}}]}
    nd = json.loads(json.dumps(d), object_hook=lambda d: N(**d))
    print(nd.child, nd.child[0].name, nd.child[0].child.name)
