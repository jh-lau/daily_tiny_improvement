"""
  @Author       : liujianhan
  @Date         : 2020/12/7 10:01
  @Project      : leetcode_in_python
  @FileName     : 861.翻转矩阵后的得分(M).py
  @Description  : 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
    移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
    在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
    返回尽可能高的分数。

    示例：
    输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
    输出：39
    解释：
    转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
    0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
    提示：
    1 <= A.length <= 20
    1 <= A[0].length <= 20
    A[i][j] 是 0 或 1
    可以这样看，n*m的每个格子都具有一个权重，其中每一行权重都自左向右递减，
    为使总和最大则尽可能使权重大的格子填“1”。最左边一列权重最大，所以总可以通过
    行翻转使左边第一列全都置“1”，后面就不能再使用行翻转了，以免破环当前的结构，
    所以考虑列翻转。对于除最左边第一列外的每一列，总可以通过列翻转使得该列“1”
    的个数不小于“0”的个数。最后所有填“1”的格子的权重和即为答案。
"""
from typing import List


class Solution:
    # 40ms, 13.5MB
    @staticmethod
    def matrix_score(A: List[List[int]]) -> int:
        n, m = len(A), len(A[0])
        for i in range(n):
            if A[i][0] == 0:
                for j in range(m):
                    A[i][j] ^= 1
        res = 0
        for i in zip(*A):
            m -= 1
            res += 2 ** m * max(i.count(1), i.count(0))

        return res


if __name__ == '__main__':
    test_cases = [
        [[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]
    ]
    for tc in test_cases:
        print(Solution.matrix_score(tc))
