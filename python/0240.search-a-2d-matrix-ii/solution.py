# Created by tg929 at 2026/09/07 09:47
# leetgo: dev
# https://leetcode.cn/problems/search-a-2d-matrix-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #右上角  左边比他小 下面比他大；左下角 右边比他大 上面比他小
        col = len(matrix[0]) - 1
        row = 0
        while col >= 0 and row < len(matrix):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().searchMatrix(matrix, target)
    print("\noutput:", serialize(ans, "boolean"))
