"""
  @Author       : liujianhan
  @Date         : 21/4/9 11:34
  @Project      : DailyTinyImprovement
  @FileName     : request_test2.py
  @Description  : Placeholder
"""
from typing import List

import grequests
import requests
import time
from colorama import Fore


def parse_request_result(response_list: List, req_number: int, start_time, async_mode: bool = False) -> None:
    failed_req = 0
    for res in response_list:
        if not res or res.status_code != 200:
            failed_req += 1
        else:
            print(res.text)
    print(Fore.GREEN, '请求成功次数', req_number - failed_req)
    print(Fore.RED, '请求失败次数', failed_req)
    print(Fore.WHITE, '请求总次数', req_number)
    string = '异步' if async_mode else '同步'
    print(Fore.GREEN, f'{string}单次请求平均耗时：', (time.time() - start_time) / req_number)


if __name__ == '__main__':
    data = {"query": "科大讯飞股份有限公"}
    req_number = 1
    url = 'http://localhost:8000/predict'
    s1 = time.time()

    req = [grequests.get(url, json=data) for _ in range(req_number)]
    result = grequests.map(req)
    parse_request_result(result, req_number, s1, True)

