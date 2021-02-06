"""
  @Author       : liujianhan
  @Date         : 2020/11/30 9:59
  @Project      : leetcode_in_python
  @FileName     : 767.重构字符串(M).py
  @Description  : 给定一个字符串S，检查是否能重新排布其中的字母，使得两相邻的字符不同。
    若可行，输出任意可行的结果。若不可行，返回空字符串。
    示例 1:
    输入: S = "aab"
    输出: "aba"
    示例 2:
    输入: S = "aaab"
    输出: ""
    注意:
    S 只包含小写字母并且长度在[1, 500]区间内。
"""
import heapq
import math
from collections import Counter


class Solution:
    # 48ms, 13.6MB
    @staticmethod
    def reorganize_string(S: str) -> str:
        length = len(S)
        if length < 3:
            return S
        counts = Counter(S)
        most_common = counts.most_common()[0]
        if most_common[1] > (length+1) // 2:
            return ''

        queue = [(-v, k) for k, v in counts.items()]
        heapq.heapify(queue)
        result = []

        while len(queue) > 1:
            _, char1 = heapq.heappop(queue)
            _, char2 = heapq.heappop(queue)
            result.extend([char1, char2])
            counts[char1] -= 1
            counts[char2] -= 1
            for char in [char1, char2]:
                if counts[char] > 0:
                    heapq.heappush(queue, (-counts[char], char))

        if queue:
            result.append(queue[0][1])

        return ''.join(result)

    # 48ms, 13.5MB
    @staticmethod
    def reorganize_string_v2(S: str) -> str:
        counts = Counter(S)
        s = sorted(counts, key=lambda x: counts[x], reverse=True)
        result = []
        for char in s:
            result += [char] * counts[char]
        ans = [0] * len(S)

        ans[::2] = result[:len(ans[::2])]
        ans[1::2] = result[len(ans[::2])::]

        if ans[0] == ans[1]:
            return ''
        else:
            return ''.join(ans)


if __name__ == '__main__':
    test_cases = [
        'aab', 'aaab', 'aabbbbccccc'
    ]
    for tc in test_cases:
        # print(Solution.reorganize_string(tc))
        print(Solution.reorganize_string_v2(tc))
