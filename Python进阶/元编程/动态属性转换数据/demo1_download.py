"""
  @Author       : liujianhan
  @Date         : 2020/10/17 11:30
  @Project      : DailyTinyImprovement
  @FileName     : demo1_download.py
  @Description  : Placeholder
"""
from urllib.request import urlopen
import warnings, os, json


URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        os.mkdir(os.path.dirname(JSON))
        warnings.warn(f"downloading {URL} to {JSON}")
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON, encoding='utf8') as fp:
        return json.load(fp)


if __name__ == '__main__':
    # feed = load()
    # print(sorted(feed['Schedule'].keys()))
    pass