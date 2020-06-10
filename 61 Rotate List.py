"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/rotate-list/
# Medium

# Linked List
# Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or not k:
            return head

        cur = head
        tail = None

        length = 0
        while cur:
            length += 1
            tail = cur
            cur = cur.next
        tail.next = head # makes the list circular

        k %= length # in case k is larger than length

        # find the division point
        cur = head
        prev = None
        for i in range(length-k):
            prev = cur
            cur = cur.next

        head = cur
        prev.next = None

        return head
