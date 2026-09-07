# Created by tg929 at 2026/09/07 14:38
# leetgo: dev
# https://leetcode.cn/problems/reverse-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().reverseList(head)
    print("\noutput:", serialize(ans, "ListNode"))
