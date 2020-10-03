"""
  @Author       : liujianhan
  @Date         : 2020/7/31 下午3:42
  @Project      : DailyTinyImprovement
  @FileName     : demo1_no_lock.py
  @Description  : Placeholder
"""
from selenium import webdriver
wd = webdriver.Chrome('driver/chromedriver')
wd.get('http://baidu.com')
wd.implicitly_wait(10)
element = wd.find_element_by_id('kw')
element.send_keys('渊亭\n')
result = wd.find_element_by_id('1')
print(result.text)