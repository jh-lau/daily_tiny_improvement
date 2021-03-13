"""
  @Author       : liujianhan
  @Date         : 21/3/12 15:33
  @Project      : DailyTinyImprovement
  @FileName     : re_demo.py
  @Description  :
"""
import re

if __name__ == '__main__':
    content_list = []
    match_subject = None
    subject_pattern = re.compile(r'([第]\w{2})*(?P<subject>[\w\s\-\d]+)([（）\s\-\da-zA-Z]*)[是]\w+')
    for cl in content_list:
        if '是' in cl:
            match_subject = subject_pattern.finditer(cl)
    subject_list = [s.groupdict() for s in match_subject if s.start() != s.end()]
    if subject_list:
        subject = subject_list[0]['subject']
