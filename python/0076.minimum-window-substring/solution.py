# Created by tg929 at 2026/08/25 10:35
# leetgo: dev
# https://leetcode.cn/problems/minimum-window-substring/

from typing import *
from leetgo_py import *

# @lc code=begin

# ```
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
# ```


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        right = 0
        left = 0
        count_t = Counter(t)
        need = len(t)
        ans = ""
        while right < len(s):
            if count_t[s[right]] > 0:
                need -= 1
            count_t[s[right]] -= 1
            right += 1
            while need == 0:
                if len(ans) == 0 or (right - left) <len(ans):
                    ans = s[left:right]
                count_t[s[left]] += 1
                if count_t[s[left]] > 0:
                    need += 1
                left += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    t: str = deserialize("str", read_line())
    ans = Solution().minWindow(s, t)
    print("\noutput:", serialize(ans, "string"))



# count_t[s[right]]  记得中括号 []取值；python 取值用 []；；；；Python 里字典和列表取值都用方括号 []，















# left = 0   #左右侧
        # right = 0
        # count_t = Counter(t)  
        # #这个的用法是 有计数，没有去查的时候；
        # # 统计每个元素出现的次数（返回特殊字典）访问不存在的元素的时候不报错，返回0
        # need = len(t)  #记录当前还需要的/还差的 数量（t 内的字母数量）。整个过程中 s  t是不变的
        # ans = ""  #用来记录需要找的 子串（字符串）
        # while right < len(s):  #整个right是要遍历一遍的
        #     if count_t[s[right]]>0:  #这个就说明当前这个 是需要的字符，
        #         need -= 1   #这样  需要的少了一个
        #     count_t[s[right]] -= 1  #不论是不是需要的 对应位置上-1，是需要的 就是-1（减少 可能变成0），不是需要的就变成负数
        #     right += 1  #向右遍历 
        #     while need == 0: #当需要的=0，也就是窗口包含了全部 t 的时候 进入内部循环
        #         if ans == "" or right - left < len(ans):  #在符合中（need=0） 找最短的
        #             ans = s[left:right]   #更新找到的这个子串，最短对应子串
        #         count_t[s[left]] += 1       # 窗口少了一个；之所以左边开始缩，是因为排除开头不需要的
        #         if count_t[s[left]] > 0:    # 如果少了之后又缺了
        #             need += 1               # 总缺的多了一个
        #         left += 1
        # return ans

#  t  s 一直都是不变的
# 但是计数 count_t 是会变的，因为counter 函数不会报错，所以遇到之前没有的也可以计算的，可以出现负数-0（针对不需要的，也不一定 需要的有可能也是负数），针对需要的就是变成0-正数
# count_t[c] 针对窗口里面 C 有多少，正数 还少这么多，0 刚好够，负数 多余了

#right 向右，代表窗口 多了一个
#left 向右，代表窗口 少了一个




#使用 counter ，不需要进行逻辑复杂混乱的 判断字符是不是属于 t 的
