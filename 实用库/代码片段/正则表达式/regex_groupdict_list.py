"""
  @Author       : liujianhan
  @Date         : 2020/1/16 下午7:18
  @Project      : DailyTinyImprovement
  @FileName     : regex_groupdict_list.py
  @Description  : Placeholder
"""
import re


def get_regex_group_list(pattern: str, target: str) -> list:
    """
    正则命名分组匹配封装
    :param pattern: 匹配模式
    :param target: 匹配目标
    :return: 匹配结果列表
    """
    matcher = re.compile(pattern)
    return [s.groupdict() for s in matcher.finditer(target) if s.start() != s.end()]
