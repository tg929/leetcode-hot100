# Created by tg929 at 2026/08/24 17:18
# leetgo: dev
# https://leetcode.cn/problems/trapping-rain-water/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def trap(self, height: List[int]) -> int:
       height_sum = [0] * len(height) #存储 水量的列表
       for i in range(len(height)):
           left_max = max(height[:i + 1])
           right_max = max(height[i:])
           height_sum[i] = max(min(left_max, right_max) - height[i],0)
       return sum(height_sum)
           

# @lc code=end

if __name__ == "__main__":
    height: List[int] = deserialize("List[int]", read_line())
    ans = Solution().trap(height)
    print("\noutput:", serialize(ans, "integer"))


#把视角打开 站在一个点上，看到左边  右边的全部个体，这样看就是要计算出正确的水位
#两端 最高的柱子围起来了水，所以左右取 各自max
#以水位是和其他柱子有关系的  水量又是和该柱子高度相关，水量=水位-柱子高度

#一定记得 先算水位  再算 水量（之间要减掉 柱子本身高度，负的就是0 ）