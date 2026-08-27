# Created by tg929 at 2026/08/27 17:51
# leetgo: dev
# https://leetcode.cn/problems/first-missing-positive/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mid = 0
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != i+1:  #注意判断条件 -需要判断 下界不可以越界
                mid = nums[nums[i]-1]  #交换两数 的标准写法：nums[nums[i]-1]，nums[i] = nums[i]，nums[nums[i]-1] 
                nums[nums[i]-1] = nums[i]
                nums[i] = mid
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().firstMissingPositive(nums)
    print("\noutput:", serialize(ans, "integer"))

#也就是把数组里面的 正整数 放在他应该放的位置上，这样叫做归位，
# 全部归位一遍之后，再来扫一遍，第一次发现 在某位置上的数字不是该数值 
# 就说明是缺这个  而这个就是缺的最小正整数