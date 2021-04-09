"""
  @Author       : liujianhan
  @Date         : 21/4/9 11:32
  @Project      : DailyTinyImprovement
  @FileName     : request_test.py
  @Description  : Placeholder
"""
from typing import List

import grequests
import requests
import time
import json
from request_test2 import parse_request_result


if __name__ == '__main__':
    data = {'params': '[{"key": "corpus", "value": "STOCK.data,FUND.data"},{"key": "type", '
                      '"value": "tllc"},{"key": "query", "value": "科大讯飞股份有限公司（以下简称“公司”）的'
                      '日常关联交易主要是公司及子公司与中国移动通信有限公司及其下属子公司、安徽淘云科技有限公司及其下'
                      '属子公司、广东爱因智能数字营销有限公司、安徽讯飞联创信息科技有限公司之间存在的采购或销售商品、提供或接'
                      '受劳务等关联交易。"}]',
            'responseType': 'Direct'}
    req_number = 10
    s1 = time.time()
    req = [grequests.post('http://localhost:8000/predict', data=data) for _ in range(req_number)]
    result = grequests.map(req)
    parse_request_result(result, req_number, s1, True)

