"""
  @Author       : liujianhan
  @Date         : 2019/12/28 下午4:28
  @Project      : DailyTinyImprovement
  @FileName     : regex_date.py
  @Description  : Placeholder
"""

import re

regex = r"((?P<pre_year>\d{4})年?[-到至])?((?P<year>\d{2,4})年)?((?P<month>\d{1,2})月)?((?P<day>\d{1,2})日)?"
pattern = re.compile(regex)
test_str = "19023年13月32日,1938年12月9日,1938年12月19日,1938年2月9日,1938年03月9日,1938年02月9日," \
           "1938年2月19日,1938年年中,1938年日内瓦医生,12月31日,3月1日,3月,12日,0月0日.1938-85年,1983-1985年," \
           "1983-943年,1938年13月193日,1938年-85年,1938年至85年,1938年到85年"

matches = pattern.finditer(test_str)
date = [s.groupdict() for s in pattern.finditer(test_str) if s.start() != s.end()]

result = []
for d in date:
    pre_year = d['pre_year'] if d['pre_year'] and int(d['pre_year']) in range(1000, 3000) else ''
    year = d['year'] if d['year'] and int(d['year']) in range(1000, 3000) else ''
    month = d['month'] if d['month'] and int(d['month']) in range(1, 13) else ''
    day = d['day'] if d['day'] and int(d['day']) in range(1, 32) else ''
    result.append(f"{year}{month}{day}")

if __name__ == '__main__':
    print(date)
    print(result)