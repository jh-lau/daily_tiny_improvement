"""
  @Author       : liujianhan
  @Date         : 2020/1/15 下午7:08
  @Project      : DailyTinyImprovement
  @FileName     : merge_duplicated_items.py
  @Description  : Placeholder
"""


def merge_duplicated_items(items: set) -> set:
    """
    合并集合中，一个元素包含另一个元素的情况，只保留长度较长的元素
    :param items: 目标集合
    :return: 合并后的集合
    """
    merged_set, temp_set_holder = set(), set()
    for t in items:
        for s in items:
            if t != s and t.find(s) != -1:
                temp_set_holder.update((t, s))
                merged_set.add(t)
    merged_set.update(items ^ temp_set_holder)
    return merged_set
