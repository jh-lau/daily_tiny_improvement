"""
  @Author       : liujianhan
  @Date         : 2020/10/13 19:28
  @Project      : DailyTinyImprovement
  @FileName     : demo2.0_多线程下载国旗1.py
  @Description  : Placeholder
"""
import asyncio
import aiohttp
import time
from demo1_顺序下载国旗 import base_url, save_flag, show, country


async def get_flag(session, cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    async with session.get(url) as resp:
        return await resp.read()


async def download_one(session, cc):
    image = await get_flag(session, cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


async def download_many(cc_list):
    async with aiohttp.ClientSession() as session:
        res = await asyncio.gather(
            *[asyncio.create_task(download_one(session, cc))
              for cc in sorted(cc_list)]
        )

    return len(res)


def main():
    t1 = time.time()
    count = asyncio.run(download_many(country))
    elapsed = time.time() - t1
    print(f"\n{count} flags downloaded in {elapsed:.2f} s")


if __name__ == '__main__':
    main()
