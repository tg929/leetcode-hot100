# Created by tg929 at 2026/08/27 20:32
# leetgo: dev
# https://leetcode.cn/problems/spiral-matrix/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top = 0
        left = 0
        bottom = len(matrix)-1
        right = len(matrix[0])-1
        result = []
        while top <=bottom  and left <= right:

            #从左走到右 top ,left---right
            for i in range(left,right+1):
                result.append(matrix[top][i])
            top += 1
            #从上走到下 right，top---bottom
            for i in range(top,bottom+1):
                result.append(matrix[i][right])
            right -= 1                              #走了这两步 之后 边界就变了
            if  top <= bottom  and left <= right :  #所以再判断一遍   ！！！！！！！！
                #从右走到左 bottom ，right----left
                for i in range(right,left-1,-1):
                    result.append(matrix[bottom][i])
                bottom -= 1
                #从下往上走 left，，bottom---top
                for i in range(bottom,top-1,-1):
                    result.append(matrix[i][left])
                left += 1
        return result



# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().spiralOrder(matrix)
    print("\noutput:", serialize(ans, "integer[]"))


#边界定义
#边界判断 以及 边界怎么累加
