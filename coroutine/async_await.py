"""
  @Author       : Liujianhan
  @Date         : 20/7/19 15:17
  @FileName     : async_await.py
  @ProjectName  : DailyTinyImprovement
  @Description  : Placeholder
 """
import types

# async def downloader(url):
#     return 'django'


@types.coroutine
def downloader(url):
    yield 'django'


async def download_url(url):
    html = await downloader(url)
    return html


if __name__ == '__main__':
    coro = download_url('http://www.baidu.com')
    coro.send(None)
