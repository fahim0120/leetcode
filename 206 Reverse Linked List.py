"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/reverse-linked-list/
# Easy
# Most Liked
# Top Interviews

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if not head:
            return None

        # p -> prev, n -> next
        p = None
        n = head.next

        while n:
            head.next = p
            p, head = head, n
            n = n.next

        head.next = p
        return head
