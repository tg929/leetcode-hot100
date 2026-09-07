# Created by tg929 at 2026/09/07 20:26
# leetgo: dev
# https://leetcode.cn/problems/linked-list-cycle-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        visited = set()  #集合表示 直接去重复；# 保存已经访问过的节点对象  如果已经存在 又访问到了，那就说明重复的，就可以返回 true了
        current = head

        while current:      #current 保存一个 ListNode 类型的节点对象；；所以集合里面存的是 保存的是节点对象本身
            if current in visited:
                return current

            visited.add(current)
            current = current.next

        return None
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    pos: int = deserialize("int", read_line())
    ans = Solution().detectCycle(head, pos)
    print("\noutput:", serialize(ans, "ListNode"))
