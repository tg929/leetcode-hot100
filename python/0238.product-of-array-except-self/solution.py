# Created by tg929 at 2026/08/27 17:10
# leetgo: dev
# https://leetcode.cn/problems/product-of-array-except-self/

from typing import *
from leetgo_py import *

# @lc code=begin

# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        left = 1
        right = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
            #注意顺序   #先把左边的计算结果存一遍
        for i in range(n-1,-1,-1):
             answer[i] *= right
             right *= nums[i]
             #注意先存后乘的顺序  #再在此基础上面 在刚刚的左边的结果之上乘右边的计算结果

        return answer
        
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().productExceptSelf(nums)
    print("\noutput:", serialize(ans, "integer[]"))
