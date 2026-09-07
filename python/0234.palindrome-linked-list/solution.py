# Created by tg929 at 2026/09/07 19:59
# leetgo: dev
# https://leetcode.cn/problems/palindrome-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_values = []
        current = head
        while current:
            list_values.append(current.val)
            current = current.next
        return list_values == list_values[::-1]

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().isPalindrome(head)
    print("\noutput:", serialize(ans, "boolean"))
