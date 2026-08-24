# Created by tg929 at 2026/08/24 11:08
# leetgo: dev
# https://leetcode.cn/problems/group-anagrams/

from typing import *
from leetgo_py import *

# @lc code=begin


# input:
# ["eat","tea","tan","ate","nat","bat"]
# output:
# [["bat"],["nat","tan"],["ate","eat","tea"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]  #存储最终结果
        for i in strs:#遍历输入列表每一个字符串（元素）
            for j in res:#遍历的是最终结果里面的每一个子列表对象（元素）
                if sorted(i)==sorted(j[0]):#一直都和第一个比较
                    j.append(i)
                    break#只比一次
            else:
                res.append([i]) #不存在异位单词的时候 直接添加元素（一级列表元素）
        return res

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().groupAnagrams(strs)
    print("\noutput:", serialize(ans, "string[][]"))
