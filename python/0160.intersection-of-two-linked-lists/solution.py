# Created by tg929 at 2026/09/07 09:46
# leetgo: dev
# https://leetcode.cn/problems/intersection-of-two-linked-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        curA, curB = headA, headB
        while curA:
            lenA += 1
            curA = curA.next    
        while curB:
            lenB += 1
            curB = curB.next
        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        else:
            for _ in range(lenB - lenA):
                headB = headB.next
        while headA and headB:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    intersectVal: int = deserialize("int", read_line())
    listA: ListNode = deserialize("ListNode", read_line())
    listB: ListNode = deserialize("ListNode", read_line())
    skipA: int = deserialize("int", read_line())
    skipB: int = deserialize("int", read_line())
    ans = Solution().getIntersectionNode(intersectVal, listA, listB, skipA, skipB)
    print("\noutput:", serialize(ans, "ListNode"))


#链表的长度获取，next
#补齐长度，同时移动指针
#判断公共交点 is
#不是公共就同时向后移动
#循环 不是到结尾 headA and headB（其实是否 一个 head A就是可以的我觉得）