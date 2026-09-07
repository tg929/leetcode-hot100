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

#第一次练习
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
#         result = []
#         left = 0
#         while (left + k) < len(nums)+1:
#             #res = 0  #每个窗口开始 初始化这个最大值，要不然放在循环外会受到前面 窗口的已经选出的最大值的影响
#             #第二次写
#             res = float('-inf')  
#             for i in range(k):
#                 res = max(res,nums[left+i])
#             result.append(res)
#             left += 1
#         return result
#第二次练习
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #使用 双端队列来存储窗口内的元素索引，保证队列头部始终是当前窗口的最大值索引
        from collections import deque
        result = []
        window = deque()  # 存储索引
        for i in range(len(nums)):  
            # 移除不在窗口范围内的索引
            if window and window[0] < i - k + 1:
                window.popleft()                     #索引过期，从队首删掉
            # 移除所有小于当前元素的索引，因为它们不可能成为最大值
            while window and nums[window[-1]] < nums[i]:
                window.pop()                         #接下来加进来的数据大于当前窗口最后的这个值的话，从队尾删掉，因为这个不可能是最大的了
            window.append(i)
            # 当窗口大小达到k时，记录当前最大值
            if i >= k - 1:
                result.append(nums[window[0]])
        return result

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSlidingWindow(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
