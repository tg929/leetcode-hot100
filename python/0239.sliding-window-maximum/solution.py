# Created by tg929 at 2026/08/25 10:18
# leetgo: dev
# https://leetcode.cn/problems/sliding-window-maximum/

from typing import *
from leetgo_py import *

# @lc code=begin

# ```
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# ```


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        left = 0
        while (left + k) < len(nums)+1:
            res = 0  #每个窗口开始 初始化这个最大值，要不然放在循环外会受到前面 窗口的已经选出的最大值的影响
            for i in range(k):
                res = max(res,nums[left+i])
            result.append(res)
            left += 1
        return result


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSlidingWindow(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
