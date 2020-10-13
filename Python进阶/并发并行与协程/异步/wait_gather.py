"""
  @Author       : Liujianhan
  @Date         : 20/7/19 20:12
  @FileName     : wait_gather.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """

import asyncio
import time


async def get_html(url):
    print(f'start get url {url}')
    await asyncio.sleep(.5)
    print(f'end get url {url}')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html('www.baidu.com') for _ in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.run_until_complete(asyncio.gather(*tasks))
    print(time.time() - start_time)

    # gather和wait的区别
    # gather更高层抽象
    tasks1 = [get_html('www.baidu.com') for _ in range(3)]
    tasks2 = [get_html('www.google.com') for _ in range(3)]
    loop.run_until_complete(asyncio.gather(*tasks1, *tasks2))
    print(time.time() - start_time)

    # 写法2
    task1 = [get_html('www.baidu.com') for _ in range(3)]
    task2 = [get_html('www.google.com') for _ in range(3)]
    task1 = asyncio.gather(*task1)
    task2 = asyncio.gather(*task2)
    # 取消事件
    task2.cancel()
    loop.run_until_complete(asyncio.gather(task1))
    print(time.time() - start_time)