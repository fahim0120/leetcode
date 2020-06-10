"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/partition-list/
# Medium

# Linked List
# Two Pointers


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:

        less_head = ListNode(0)
        more_head = ListNode(0)

        less = less_head
        more = more_head

        cur = head
        while cur:
            if cur.val < x:
                less.next = cur
                less = less.next
            else:
                more.next = cur
                more = more.next

            cur = cur.next

        more.next = None
        less.next = more_head.next
        return less_head.next
