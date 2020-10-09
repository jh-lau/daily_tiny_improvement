"""
  @Author       : liujianhan
  @Date         : 2020/10/9 11:56
  @Project      : DailyTinyImprovement
  @FileName     : demo_tenacity.py
  @Description  : Placeholder
"""
from tenacity import retry, wait_fixed, stop_after_attempt, stop_after_delay, retry_if_result
from tenacity import retry_if_exception_type
from requests import exceptions


@retry
def test_retry1():
    print('等待重试，重试无间隔执行。。。')
    raise Exception


@retry(wait=wait_fixed(2))
def test_retry2():
    print('等待重试，重试2秒间隔。')
    raise Exception


@retry(stop=stop_after_delay(2))
def test_retry3():
    print('重试2秒后退出。。。')
    raise Exception


@retry(stop=stop_after_attempt(2))
def test_retry4():
    print('重试2次后退出。。。')
    raise Exception


@retry(stop=(stop_after_attempt(2) | stop_after_delay(1)))
def test_retry5():
    print('重试2次或者2秒后退出。。。')
    raise Exception


@retry(retry=retry_if_exception_type(exceptions.Timeout))
def test_retry6():
    print('连接超时后重试')
    raise exceptions.Timeout


def is_false(value):
    return not value


@retry(stop=stop_after_attempt(3),
       retry=retry_if_exception_type(is_false))
def test_retry7():
    print('不符合条件后重试')
    return False


@retry(stop=stop_after_attempt(7), reraise=True)
def test_retry8():
    print("重试后抛出原始异常")
    raise Exception


def return_last_value(retry_state):
    print("执行回调函数")
    return retry_state.outcome.result()  # 表示返回原函数的返回值


@retry(stop=stop_after_attempt(3),
       retry_error_callback=return_last_value,
       retry=retry_if_result(is_false))
def test_retry9():
    print("等待重试中...")
    return False


if __name__ == '__main__':
    test_retry9()
