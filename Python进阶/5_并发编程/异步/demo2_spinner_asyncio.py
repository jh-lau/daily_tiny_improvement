"""
  @Author       : liujianhan
  @Date         : 2020/10/15 15:28
  @Project      : DailyTinyImprovement
  @FileName     : demo2_spinner_asyncio.py
  @Description  : Placeholder
"""
import asyncio
import itertools


async def spin(msg):  # 2
    for char in itertools.cycle('|/-\\'):  # 3
        status = f'{char} {msg}'
        print(f"\r{status}", end='')
        try:
            await asyncio.sleep(1.)
        except asyncio.CancelledError:
            break


async def slow_function():
    await asyncio.sleep(3)
    return 42


async def supervisor():
    spinner = asyncio.create_task(spin('thinking!'))
    print('spinner object:', spinner)
    result = await slow_function()
    spinner.cancel()
    return result


def main():
    result = asyncio.run(supervisor())
    print('\rAnswer:', result)


if __name__ == '__main__':
    main()
