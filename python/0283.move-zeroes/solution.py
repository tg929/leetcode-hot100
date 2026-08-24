# Created by tg929 at 2026/08/24 14:56
# leetgo: dev
# https://leetcode.cn/problems/move-zeroes/

from typing import *
from leetgo_py import *

# @lc code=begin

# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    Solution().moveZeroes(nums)
    ans = nums
    print("\noutput:", serialize(ans, "List[int]"))


#很巧妙的使用这两个 列表的 移除和添加 元素   “0” 这个元素的移动 其实就是删除和添加的过程