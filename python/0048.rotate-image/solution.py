# Created by tg929 at 2026/08/28 16:19
# leetgo: dev
# https://leetcode.cn/problems/rotate-image/

from typing import *
from leetgo_py import *

# @lc code=begin

#矩阵的行变成列

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n//2):
            matrix[i],matrix[n-1-i] = matrix[n-1-i],matrix[i]
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    Solution().rotate(matrix)
    ans = matrix
    print("\noutput:", serialize(ans, "List[List[int]]"))


#一步做很复杂 分多步
# 行的交换，元素的交换
# 列的转换 / 矩阵的转置
#  代码实现即是：
# for i in range(n):
#             for j in range(i+1,n):
#                 matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]