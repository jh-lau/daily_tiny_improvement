"""
  @Author       : liujianhan
  @Date         : 2020/10/13 19:28
  @Project      : DailyTinyImprovement
  @FileName     : demo2.0_多线程下载国旗1.py
  @Description  : 单线程异步
"""
import asyncio
import aiohttp
from demo1_顺序下载国旗 import base_url, save_flag, show, main


@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = yield from aiohttp.ClientSession().get(url)
    image = yield from resp.read()
    return image


@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, save_flag, image, cc+'.jpg')
    return cc


def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in sorted(cc_list)]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()

    return len(res)


if __name__ == '__main__':
    main(download_many)
