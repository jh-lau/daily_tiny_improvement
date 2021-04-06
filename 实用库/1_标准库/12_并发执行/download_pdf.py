"""
  @Author       : liujianhan
  @Date         : 2020/11/13 19:27
  @Project      : DailyTinyImprovement
  @FileName     : pdf下载.py
  @Description  : 如果报错，确认：
    requests[security]==2.7.0  # not 2.18.1
    cryptography==1.9  # not 2.0
"""
import os
import re
import time
from concurrent.futures import ProcessPoolExecutor

import requests


def get_file_content(title_link: tuple):
    title, pdf_url = title_link
    title = f'{title}.pdf'
    r = requests.get(pdf_url)
    print(f"{title} 开始下载。。。。")
    with open(title, 'wb') as f:
        f.write(r.content)
    print(f"{title} 下载完成。")


if __name__ == '__main__':
    url = 'https://hub.baai.ac.cn/view/3675'
    res = requests.get(url, verify=False)
    # print(res.text)
    link_pattern = re.compile('<strong>(.*)<\/strong>.*href="(https.*)"')
    link_result = link_pattern.findall(res.text)
    t1 = time.time()
    # 1.单线程串行下载耗时：Time costs: 391.487 s
    # for tl in link_result:
    #     get_file_content(tl)

    # 2.8线程耗时：Time costs: 178.355 s
    # with ThreadPoolExecutor(8) as pool:
    #     pool.map(get_file_content, link_result)

    # 3.与待下载任务同数量线程耗时：Time costs: 144.8 s
    # with ThreadPoolExecutor(max(20, len(link_result))) as pool:
    #     pool.map(get_file_content, link_result)

    # 4.满进程程耗时：Time costs: 146.45 s
    with ProcessPoolExecutor(min(16, os.cpu_count())) as pool:
        pool.map(get_file_content, link_result)
    print(f"Time costs: {time.time() - t1:.3f} s")
