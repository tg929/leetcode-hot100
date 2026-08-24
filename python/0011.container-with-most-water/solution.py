# Created by tg929 at 2026/08/24 15:06
# leetgo: dev
# https://leetcode.cn/problems/container-with-most-water/

from typing import *
from leetgo_py import *

# @lc code=begin

# input:
# [1,8,6,2,5,4,8,3,7]
# output:
# 49


class Solution:
    # def maxArea(self, height: List[int]) -> int:
    #     left = 0
    #     right = len(height) - 1
    #     max_area = 0
    #     for i in range(len(height)):
    #         area = min(height[left], height[right]) * (right - left)
    #         max_area = max(max_area, area)
    #         left = i
    #     return max_area
     def maxArea(self, height: List[int]) -> int:  #正确解法，并不是去单纯遍历
           left = 0
           right = len(height) - 1
           max_area = 0
           while left < right:
               area = min(height[left], height[right]) * (right - left)
               max_area = max(max_area, area)
               if height[left] < height[right]:#永远移动矮的一侧
                   left += 1
               else:
                   right -= 1
           return max_area

# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxArea(height)
    print("\noutput:", serialize(ans, "integer"))


#双指针
#们永远移动矮的那边，跳过所有"确定不会更优"的情况。

#正确做法