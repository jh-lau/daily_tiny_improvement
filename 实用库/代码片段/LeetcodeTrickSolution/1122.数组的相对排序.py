"""
  @Author       : liujianhan
  @Date         : 2020/11/14 11:58
  @Project      : leetcode_in_python
  @FileName     : 1122.数组的相对排序.py
  @Description  : 给你两个数组，arr1 和 arr2，
    arr2 中的元素各不相同
    arr2 中的每个元素都出现在 arr1 中
    对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。
    示例：
    输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
    输出：[2,2,2,1,4,3,3,9,6,7,19]
    提示：

    arr1.length, arr2.length <= 1000
    0 <= arr1[i], arr2[i] <= 1000
    arr2 中的元素 arr2[i] 各不相同
    arr2 中的每个元素 arr2[i] 都出现在 arr1 中
"""
from typing import List


class Solution:
    # 52ms, 13.8MB
    @staticmethod
    def relative_sort_array(arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        not_in_arr2 = sorted([s for s in arr1 if s not in set(arr2)])
        for num in arr2:
            for _ in range(arr1.count(num)):
                result.append(num)
        result.extend(not_in_arr2)

        return result

    # 36ms, 13.7MB
    @staticmethod
    def relative_sort_array_v2(arr1: List[int], arr2: List[int]) -> List[int]:
        offset = len(arr2)
        count = {num: i for i, num in enumerate(arr2)}
        arr1.sort(key=lambda x: count.get(x, x+offset))

        return arr1


if __name__ == '__main__':
    test_cases = [
        ([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]),
        ([26, 21, 11, 20, 50, 34, 1, 18], [21, 11, 26, 20])
    ]
    for tc in test_cases:
        print(Solution.relative_sort_array(*tc))
        print(Solution.relative_sort_array_v2(*tc))
