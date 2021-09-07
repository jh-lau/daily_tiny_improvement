"""
  @Author       : liujianhan
  @Date         : 21/9/7 22:42
  @Project      : DailyTinyImprovement
  @FileName     : douban_movie.py
  @Description  : Placeholder
"""
from functools import partial

import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
import pandas as pd


def get_cover_pic(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    print(f'current url: {url}')
    r = requests.get(url, headers=header, verify=True)
    print(r.status_code, r.text)
    soup = BeautifulSoup(r.text, 'html.parser')
    target = [t['src'] for t in soup.find_all('img') if t.attrs.get('title') == '点击看更多海报']  # for movie
    return f"{url},{target}" if target else f"{url},"


if __name__ == '__main__':
    df = pd.read_csv('douban_movie.csv')
    target_urls = df['链接'].to_list()[:1]
    result = []
    with ThreadPoolExecutor(20) as executor:
        res = executor.map(get_cover_pic, sorted(target_urls))
        for r in res:
            result.append(r)
    print('writing to file.....')
    with open('movie_cover.txt', encoding='utf8', mode='w') as file:
        for s in result:
            print(s)
            file.writelines(s + '\n')
