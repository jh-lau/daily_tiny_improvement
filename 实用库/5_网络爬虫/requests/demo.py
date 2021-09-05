"""
  @Author       : liujianhan
  @Date         : 21/9/5 0:30
  @Project      : DailyTinyImprovement
  @FileName     : demo.py
  @Description  :
"""
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'https://book.douban.com/subject/24531334/'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    r = requests.get(url, headers=header, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    target = [t['src'] for t in soup.find_all('img') if t.attrs.get('title') == '点击看大图']  # for book
    # target = [t['src'] for t in soup.find_all('img') if t.attrs.get('title') == '点击看更多海报']  # for movie
    pass