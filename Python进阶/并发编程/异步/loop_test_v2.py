"""
  @Author       : Liujianhan
  @Date         : 20/7/19 20:02
  @FileName     : loop_test_v2.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """

import asyncio
import time
from functools import partial  # 用于直接收一个参数，但是有多个参数需要传入的情况


async def get_html(url):
    print('start get url')
    await asyncio.sleep(.5)
    return 'django'


def callback(url, future):
    print('get url ', url)
    print('send email to django')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()

    # method1：获取协程返回值以及添加回调函数
    # get_future = asyncio.ensure_future(get_html('www.baidu.com'))
    # callback只能接收一个参数，因此需要用partial进行封装
    # get_future.add_done_callback(callback)
    # loop.run_until_complete(get_future)
    # print(get_future.result())

    # method2：获取协程返回值以及添加回调函数
    task = loop.create_task(get_html('www.baidu.com'))
    # callback只能接收一个参数，因此需要用partial进行封装
    task.add_done_callback(partial(callback, 'www.google.com'))
    loop.run_until_complete(task)
    print(task.result())
