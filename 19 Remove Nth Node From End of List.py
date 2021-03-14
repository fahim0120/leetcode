"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Medium
# Most Liked
# Top Interviews


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        begin = ListNode(next=head)
        fast = slow = begin
        for i in range(n):
            fast = fast.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        temp = slow.next
        slow.next = slow.next.next
        del temp

        head = begin.next
        del begin

        return head
