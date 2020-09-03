"""
  @Author       : liujianhan
  @Date         : 20/9/3 22:21
  @Project      : DailyTinyImprovement
  @FileName     : autoscraper_test.py
  @Description  : https://github.com/alirezamika/autoscraper
"""
from autoscraper import AutoScraper
from pprint import pprint as print

url = 'https://stackoverflow.com/questions/2081586/web-scraping-with-python'

wanted_list = ["How to call an external command?"]

scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)