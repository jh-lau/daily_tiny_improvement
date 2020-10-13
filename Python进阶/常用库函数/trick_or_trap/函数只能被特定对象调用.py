"""
  @Author       : liujianhan
  @Date         : 2020/10/9 15:56
  @Project      : DailyTinyImprovement
  @FileName     : 函数只能被特定对象调用.py
  @Description  : Placeholder
"""
import inspect
from functools import wraps


def foot_up():
    stack = inspect.stack()
    prev_func = stack[1].function
    if prev_func != 'jump':
        print(f'非指定函数调用 {prev_func}，拒绝执行后续代码')
        return
    else:
        print(f'指定函数调用 {prev_func}，允许继续执行')
        print('双脚离地')


def jump():
    print('既然是跳舞，肯定要跳起来')
    foot_up()


def dance():
    print('开始跳舞')
    foot_up_new()
    # jump()


def call_stack_check(valid_function_list=None):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if valid_function_list:
                stack = inspect.stack()
                prev_func_name = stack[1].function
                if prev_func_name not in valid_function_list:
                    raise Exception('不是指定函数调用列表调用，拒绝执行后续代码')
                else:
                    print('指定函数列表的函数调用，执行后续代码')
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorate


@call_stack_check(['jump'])
def foot_up_new():
    print('双脚离地')


if __name__ == '__main__':
    dance()
