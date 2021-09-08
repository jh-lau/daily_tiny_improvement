"""
  @Author       : liujianhan
  @Date         : 21/9/7 22:42
  @Project      : DailyTinyImprovement
  @FileName     : douban_movie.py
  @Description  : Placeholder
"""

from concurrent.futures import ProcessPoolExecutor
from time import sleep

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_cover_pic(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    }

    sleep(np.random.randint(0, 3))
    r = requests.get(url, headers=header, verify=True)
    soup = BeautifulSoup(r.text, 'html.parser')
    target = [t['src'] for t in soup.find_all('img') if t.attrs.get('title') == '点击看更多海报']  # for movie
    return f"{url},{target[0]}" if target else f"{url},"


if __name__ == '__main__':
    df = pd.read_csv('douban_movie.csv')
    target_urls = sorted(df['链接'].to_list())[:1]
    count = 0
    with open('movie_cover.txt', encoding='utf8', mode='a') as file:
        with ProcessPoolExecutor(4) as executor:
            res = executor.map(get_cover_pic, target_urls)
            for r in res:
                count += 1
                print(f'\r {count} -- {r}', end='')
                file.writelines(r + '\n')

