"""
  @Author       : liujianhan
  @Date         : 2020/11/13 19:27
  @Project      : DailyTinyImprovement
  @FileName     : pdf下载.py
  @Description  : 如果报错，确认：
    requests[security]==2.7.0  # not 2.18.1
    cryptography==1.9  # not 2.0
"""
import requests
import re


def get_file_content(url, file):
    r = requests.get(url)
    with open(file, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    url = 'https://hub.baai.ac.cn/view/3675'
    res = requests.get(url, verify=False)
    # print(res.text)
    link_pattern = re.compile('<strong>(.*)<\/strong>.*href="(https.*)"')
    print(link_pattern.findall(res.text))
    # get_file_content(url, 'test.pdf')