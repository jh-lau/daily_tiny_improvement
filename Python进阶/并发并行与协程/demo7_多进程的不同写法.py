"""
  @Author       : liujianhan
  @Date         : 2020/10/15 14:47
  @Project      : DailyTinyImprovement
  @FileName     : demo7_多进程的不同写法.py
  @Description  : Placeholder
"""
from .demo6_多进程测试 import gen_point_list, calc_distance
import multiprocessing as mp
import time

# 写法1
s = gen_point_list(10)
t3 = time.time()
jobs = []
for i in range(4):
    jobs.append(mp.Process(target=calc_distance, args=(next(s),)))
for j in jobs:
    j.start()
for j in jobs:
    j.join()
print(f"Multi-processing process time cost: {time.time() - t3: .3f} seconds")


# 写法2：from spert
def process_configs(target, arg_parser):
    args, _ = arg_parser.parse_known_args()
    ctx = mp.get_context('fork')

    for run_args, _run_config, _run_reapeat in _yield_configs(arg_parser, args):
        p = ctx.Process(target=target, args=(run_args, ))
        p.start()
        p.join()
