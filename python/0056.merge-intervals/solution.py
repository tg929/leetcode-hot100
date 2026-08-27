# Created by tg929 at 2026/08/27 15:15
# leetgo: dev
# https://leetcode.cn/problems/merge-intervals/

from typing import *
from leetgo_py import *

# @lc code=begin

# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()#Python 里对二维列表排序：
        for interval in intervals:
            if len(result) != 0 and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1],interval[1])
            else:
                result.append(interval)
        return result
# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().merge(intervals)
    print("\noutput:", serialize(ans, "integer[][]"))
