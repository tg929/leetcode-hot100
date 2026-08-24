# Created by tg929 at 2026/08/24 20:41
# leetgo: dev
# https://leetcode.cn/problems/find-all-anagrams-in-a-string/

from typing import *
from leetgo_py import *
# @lc code=begin

from collections import Counter

# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #p:window
        #window_len:len(p)
        counter_p = Counter(p)
        window_len = len(p)
        left = 0
        res = []
        for left in range(len(s)):
            if counter_p == Counter(s[left:left + window_len]):
                res.append(left)
        return res
            

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    p: str = deserialize("str", read_line())
    ans = Solution().findAnagrams(s, p)
    print("\noutput:", serialize(ans, "integer[]"))

#类比 上一题目，这一题目是 滑动窗口是固定的；
#

# from collections import Counter
#    Counter("abc")   # → {'a': 1, 'b': 1, 'c': 1}
#    Counter("abbc")  # → {'a': 1, 'b': 2, 'c': 1}
#  ```

#  那判断异位词就变成了什么？

#  如果两个 Counter 相等，就是异位词：

#  ```python
#    Counter("abc") == Counter("cba")  # True
#    Counter("abc") == Counter("abb")  # False
#  ```