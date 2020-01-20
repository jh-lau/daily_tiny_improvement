"""
  @Author       : liujianhan
  @Date         : 2020/1/20 下午8:01
  @Project      : DailyTinyImprovement
  @FileName     : regex_pattern.py
  @Description  : Placeholder
"""


def extract_special_weapon_entity(event: str,
                                  special_ending: list = []) -> list:

    if not special_ending:
        return []
    match_ending = '|'.join(special_ending)
    pattern = f'(?P<target>“\w+”(（[\w\-\d]+）)?\-?\s?[\w\d\s]*?({match_ending})+)'

    return get_regex_group_list(pattern, event)
