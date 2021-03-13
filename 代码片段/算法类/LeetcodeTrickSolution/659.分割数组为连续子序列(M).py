"""
  @Author       : liujianhan
  @Date         : 2020/12/4 16:13
  @Project      : leetcode_in_python
  @FileName     : 659.分割数组为连续子序列(M).py
  @Description  : 给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，
    其中每个子序列都由连续整数组成且长度至少为 3 。
    如果可以完成上述分割，则返回 true ；否则，返回 false 。

    示例 1：
    输入: [1,2,3,3,4,5]
    输出: True
    解释:
    你可以分割出这样两个连续子序列 :
    1, 2, 3
    3, 4, 5

    示例 2：
    输入: [1,2,3,3,4,4,5,5]
    输出: True
    解释:
    你可以分割出这样两个连续子序列 :
    1, 2, 3, 4, 5
    3, 4, 5

    示例 3：
    输入: [1,2,3,4,4,5]
    输出: False

    提示：
    输入的数组长度范围为 [1, 10000]
    通过次数7,789提交次数16,373
"""
import collections
import heapq
from typing import List


class Solution:
    # 228ms, 14.7MB
    @staticmethod
    def is_possible(nums: List[int]) -> bool:
        mp = collections.defaultdict(list)
        for x in nums:
            queue = mp.get(x - 1)
            if queue:
                prev_length = heapq.heappop(queue)
                heapq.heappush(mp[x], prev_length + 1)
            else:
                heapq.heappush(mp[x], 1)

        return not any(queue and queue[0] < 3 for queue in mp.values())


if __name__ == '__main__':
    test_cases = [
        [1, 2, 3, 3, 4, 5],
        [1, 2, 3, 3, 4, 4, 5, 5],
        [1, 2, 3, 4, 4, 5]
    ]
    for tc in test_cases:
        print(Solution.is_possible(tc))
