# Created by tg929 at 2026/08/27 19:51
# leetgo: dev
# https://leetcode.cn/problems/set-matrix-zeroes/

from typing import *
from leetgo_py import *

# @lc code=begin

# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        rows = [False] * m
        cols = [False] * n

        # 第一遍：扫矩阵，标记哪些行/列有 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        # 第二遍：根据标记置零
        for i in range(m):
            for j in range(n):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
                

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    Solution().setZeroes(matrix)
    ans = matrix
    print("\noutput:", serialize(ans, "List[List[int]]"))
