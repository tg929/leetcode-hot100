# Created by tg929 at 2026/08/24 16:26
# leetgo: dev
# https://leetcode.cn/problems/3sum/

from typing import *
from leetgo_py import *

# @lc code=begin


# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        return result

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().threeSum(nums)
    print("\noutput:", serialize(ans, "integer[][]"))


#暴力：三层循环

#解题思路就是：nums[j] + nums[k] = -nums[i]  逻辑的转换，成为两数之和的问题，两数之和高效解法--双指针

# 也就是其实 右侧right一开始是固定的，left始终都是在 当前i的下一个位置上，
# 三者之和大的话 （right只能向左 left只能向右），right向左（已经排序），小的话 就left向右。直
#  到=0，就是找到了一组，
#  去重的话  就是 两个紧挨着的相等的话 就跳过，因为 
# 在一次确定遍历结果里面 right left是不变的 当 i 和  i-1 对应的值相等的话 就直接排除一个，因为结果是一模一样