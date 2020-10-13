"""
  @Author       : liujianhan
  @Date         : 2020/10/13 19:17
  @Project      : DailyTinyImprovement
  @FileName     : demo1_顺序下载国旗.py
  @Description  : Placeholder
"""
import os, time, sys, requests

country = 'CN IN US ID BR PK NG BD RU JP MX PH VN ET EG DE IR TR CD FR'.split()
base_url = 'http://flupy.org/data/flags'
dest = 'downloaded_flags/'


def save_flag(img, filename):
    path = os.path.join(dest, filename)
    with open(path, 'wb') as fp:
        fp.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(base_url, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def download_many(cc_list):
    for cc in sorted(cc_list):
        image = get_flag(cc)
        show(cc)
        save_flag(image, cc.lower() + '.gif')
    return len(cc_list)


def main(download_many):
    t1 = time.time()
    count = download_many(country)
    time_elapsed = time.time() - t1
    print(f"\n{count} flags downloaded in {time_elapsed:.2f} s")


if __name__ == '__main__':
    main(download_many)
