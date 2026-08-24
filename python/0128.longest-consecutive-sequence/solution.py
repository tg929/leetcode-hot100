# Created by tg929 at 2026/08/24 11:31
# leetgo: dev
# https://leetcode.cn/problems/longest-consecutive-sequence/

from typing import *
from leetgo_py import *

# @lc code=begin

# input:
# [100,4,200,1,3,2]
# output:
# 4

# input:
# [1,0,1,2]
# output:
# 3

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        sorted_nums = sorted(nums_set) #排序
        for i in range(len(sorted_nums)):#遍历找紧挨着的序列
        #     if i > 0 and sorted_nums[i] == sorted_nums[i - 1] + 1:
        #         continue   #从第二个元素开始 如果 当前元素是前一个元素+1 就继续循环
        #     else: #如果是第一个元素  或者 当前元素不是前一个元素+1 
            start = sorted_nums[i] #向后移
            length = 1  #最小是1
            while start + length in nums_set:#如果当前元素+1 在集合里 就继续循环
                length += 1#长度++
            return length

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestConsecutive(nums)
    print("\noutput:", serialize(ans, "integer"))


#整体就是
#1.去重  排序 都有必要
#2.定义左边标兵 逐渐右移 
#3.计算 这个左边标兵+1 是否在原列表
#4.记录长度的变量进行++