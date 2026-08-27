# Created by tg929 at 2026/08/27 16:42
# leetgo: dev
# https://leetcode.cn/problems/rotate-array/

from typing import *
from leetgo_py import *

# @lc code=begin

# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #后k个  nums[-k:]
        #余下的 nums[:len(nums)-k-1]
        #nums[:] = nums[-k:]+nums[:len(nums)-k] #但是没考虑 k 很大的时候，所以更好的如下
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    Solution().rotate(nums, k)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))


 #一直都是 最后一个 放在第一个。其他一次后移动
