# Created by tg929 at 2026/08/24 20:01
# leetgo: dev
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        window = set()
        for right in range(len(s)):
            while s[right] in window:
                left += 1
                window.remove(s[left - 1])
            window.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length

            

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().lengthOfLongestSubstring(s)
    print("\noutput:", serialize(ans, "integer"))


#巧用集合的 in , remove, add 方法，来维护一个滑动窗口，窗口内的元素都是不重复的
#