"""
  @Author       : liujianhan
  @Date         : 21/9/5 15:27
  @Project      : DailyTinyImprovement
  @FileName     : douban_book.py
  @Description  : 获取豆瓣书籍封面
"""
import re

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_cover_pic(url):
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    r = requests.get(url, headers=header, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    target = [t['src'] for t in soup.find_all('img') if t.attrs.get('title') == '点击看大图']
    return target[0] if target else ''


if __name__ == '__main__':
    book_name_mapper = {'简介': 'inf', '标题': 'title', '豆瓣评分': 'rate', '链接': 'link', '创建时间': 'create_date',
                        '我的评分': 'my_rate',
                        '标签': 'label',
                        '评论': 'comment'}
    book_name_mapper_after = {
        "title": "书名",
        "rate": "豆瓣评分",
        "my_rate": "个人评分",
        "author": "作者",
        "country": "国家",
        "trans": "译者",
        "series": "系列",
        "create_date": "阅读时间",
        "read_state": "阅读状态",
        "pub_date": '出版时间',
        "label": "标签",
        "pub_org": "出版社",
        "weixin_read": "微信读书",
        "link": "豆瓣链接",
        "cover": "封面"
    }
    path = r'C:\\Users\\Administrator\\Desktop\\lectures\\豆伴(146232214).csv'
    df = pd.read_csv(path)
    df.rename(inplace=True, columns=book_name_mapper)
    df['country'] = df.inf.apply(lambda x: re.findall(r'[【（\(\[](\w+)[\)\]）】]', x))
    df.country = df.country.apply(lambda x: x[0] if x else '中')
    df['pub_org'] = df.inf.apply(lambda x: x.rsplit('/', 1)[-1])
    df['pub_date'] = df.inf.apply(lambda x: re.findall(r'\d{4}', x))
    df.pub_date = df.pub_date.apply(lambda x: x[0] if x else '')
    df['author'] = df.inf.apply(lambda x: x.split('/')[0])
    df.my_rate = df.my_rate.apply(lambda x: int(x) * '⭐')
