# Created by tg929 at 2026/08/23 20:04
# leetgo: dev
# https://leetcode.cn/problems/two-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]  #执行到这里就会直接停止/终止函数的执行，所以只找一组而且是第一组

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())  #将读取到的内容转换成 list
    target: int = deserialize("int", read_line())   #将读取到的内容转换成 int
    ans = Solution().twoSum(nums, target)
    print("\noutput:", serialize(ans, "integer[]"))
