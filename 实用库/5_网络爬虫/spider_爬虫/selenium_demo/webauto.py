"""
  @Author       : liujianhan
  @Date         : 2020/7/31 下午3:08
  @Project      : DailyTinyImprovement
  @FileName     : webauto.py
  @Description  : Placeholder
"""
from selenium import webdriver

wd = webdriver.Chrome('driver/chromedriver')
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
element = wd.find_element_by_id('container')
spans = element.find_elements_by_tag_name('span')
print([span.text for span in spans])
# elements = wd.find_elements_by_class_name('animal')
# elements = wd.find_elements_by_tag_name('div')
# for element in elements:
#     print(element.text)
# element = wd.find_element_by_id('kw')
# element.send_keys('渊亭\n')
