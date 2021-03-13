"""
  @Author       : liujianhan
  @Date         : 2020/11/28 10:47
  @Project      : leetcode_in_python
  @FileName     : 493.翻转对(H).py
  @Description  : 给定一个数组 nums ，如果 i < j 且 nums[i] > 2*nums[j] 我们就将 (i, j) 称作一个重要翻转对。
    你需要返回给定数组中的重要翻转对的数量。
    示例 1:
    输入: [1,3,2,3,1]
    输出: 2
    示例 2:
    输入: [2,4,3,5,1]
    输出: 3
    注意:
    给定数组的长度不会超过50000。
    输入数组中的所有数字都在32位整数的表示范围内。
"""
import bisect
from typing import List


class Solution:
    # 2676ms, 20.6MB
    @staticmethod
    def reverse_pairs(nums: List[int]) -> int:
        tb, res = [], 0
        for n in nums[::-1]:
            res += bisect.bisect_left(tb, n)
            n2 = 2 * n
            idx = bisect.bisect_left(tb, n2)
            tb.insert(idx, n2)

        return res

    # 1576ms, 20.7MB
    @staticmethod
    def reverse_pairs_v2(nums: List[int]) -> int:
        ans = 0

        def merge_sort(nums):
            nonlocal ans
            if len(nums) <= 1:  # 不能写 == 0 否则死循环
                return nums
            mid = len(nums) >> 1
            left, right = merge_sort(nums[:mid]), merge_sort(nums[mid:])
            for i in right:
                add = len(left) - bisect.bisect(left, i * 2)
                if not add:  # 说明 right 剩下的元素的 2 倍都不可能在 left 里
                    break
                ans += add
            return sorted(left + right)
            # left+right 和 nums 不同的是前者两部分已排过序，后者为排序，这对 sorted 效率影响较大

        merge_sort(nums)
        return ans


if __name__ == '__main__':
    test_cases = [
        [1, 3, 2, 3, 1],
        [2, 4, 3, 5, 1]
    ]
    for tc in test_cases:
        print(Solution.reverse_pairs(tc))
        print(Solution.reverse_pairs_v2(tc))
