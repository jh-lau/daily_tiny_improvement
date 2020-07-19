"""
  @Author       : Liujianhan
  @Date         : 20/7/19 19:51
  @FileName     : loop_test.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import asyncio
import time


async def get_html(url):
    print('start get url')
    await asyncio.sleep(2)  # 2s
    # time.sleep(2)  # 同步io -> 20s
    print('end get url')


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    tasks = [get_html('www.baidu.com') for _ in range(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)
