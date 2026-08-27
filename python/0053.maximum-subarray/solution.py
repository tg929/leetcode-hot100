# Created by tg929 at 2026/08/27 13:24
# leetgo: dev
# https://leetcode.cn/problems/maximum-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin

# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = nums[0]
        for i in range(len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxSubArray(nums)
    print("\noutput:", serialize(ans, "integer"))




#不要混淆子数组 和 子序列;子数组 有顺序需要连续，子序列 有顺序不需要连续
# 连续子数组就是 子序列

#不要想复杂了
#一旦自己开始枚举很多种判断情况的时候 就说明自己考虑的复杂了，这个时候就要想可能实现逻辑很简单。