# Created by tg929 at 2026/08/24 21:10
# leetgo: dev
# https://leetcode.cn/problems/subarray-sum-equals-k/

from typing import *
from leetgo_py import *

# @lc code=begin

# 输入：nums = [1,1,1], k = 2
# 输出：2

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0   
        prefix = 0
        prefix_dict = {0: 1}  
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - k in prefix_dict:
                count += prefix_dict[prefix - k]
            prefix_dict[prefix] = prefix_dict.get(prefix, 0) + 1
        return count

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().subarraySum(nums, k)
    print("\noutput:", serialize(ans, "integer"))


# 思路：有点像那个计算水量的题目
# 记下每一个位置上的 从头开始的累加和
# 每一个位置上的 累加和-k 如果在此之前出现过，就说明存在按照题目符合的子数组
# 统计每一个位置上累加和（整个数组上每一个位置上的） 出现的次数
# 这个次数就是  每一个位置上对应的次数 累加成为最终count