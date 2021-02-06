"""
  @Author       : liujianhan
  @Date         : 20/11/15 0:36
  @Project      : leetcode_in_python
  @FileName     : 594.最长和谐子序列.py
  @Description  : 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
    现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
    示例 1:

    输入: [1,3,2,2,5,2,3,7]
    输出: 5
    原因: 最长的和谐数组是：[3,2,2,2,3].
    说明: 输入的数组长度最大不超过20,000.
"""
from collections import Counter
from typing import List


class Solution:
    # 144ms, 14.9MB
    @staticmethod
    def find_LHS(nums: List[int]) -> int:
        count = Counter(nums)
        keys = sorted(list(count.keys()))
        result = [count[keys[i]] + count[keys[i+1]] for i in range(len(keys)-1)
                  if abs(keys[i] - keys[i+1]) == 1]
        return max(result) if result else 0

    # 72ms, 14.7MB
    @staticmethod
    def find_LHS_v2(nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for key in count:
            if key + 1 in count:
                res = max(res, count[key] + count[key+1])

        return res


if __name__ == '__main__':
    test_cases = [
        [1, 3, 2, 2, 5, 2, 3, 7],
        [1, 1, 1, 1],
        [1, 3, 5, 7, 9, 11, 13, 15, 17],
    ]
    for tc in test_cases:
        print(Solution.find_LHS(tc))
        print(Solution.find_LHS_v2(tc))
