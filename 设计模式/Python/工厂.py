"""
  @Author       : liujianhan
  @Date         : 2020/11/14 14:57
  @Project      : DailyTinyImprovement
  @FileName     : 工厂.py
  @Description  : Placeholder
"""
from typing import Union


class EnglishLocalizer:
    def __init__(self):
        self.translation = {
            'hello': "你好",
            'goodbye': "再见"
        }

    def localize(self, msg: str) -> str:
        return self.translation.get(msg, '我听不懂你在说什么')


class ChineseLocalizer:
    def localize(self, msg: str) -> str:
        return msg


def get_localize(language: str = 'Chinese'):
    localizers = {
        'Chinese': ChineseLocalizer,
        'English': EnglishLocalizer
    }

    return localizers[language]()


if __name__ == '__main__':
    c, e = get_localize(), get_localize("English")
    print(c.localize('你好'))
    print(e.localize('你好'))
    print(c.localize('hello'))
    print(e.localize('hello'))
    print(e.localize('goodbye'))
