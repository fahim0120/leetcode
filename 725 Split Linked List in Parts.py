"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/split-linked-list-in-parts/
# Medium

# Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:

        # find length of the list
        leng = 0
        curr = root
        while curr:
            leng += 1
            curr = curr.next

        width, remainder = divmod(leng, k)

        result = []
        curr = root
        prev = None
        for i in range(k):
            result.append(curr)

            if i < remainder:
                part_leng = width + 1
            else:
                part_leng = width

            for _ in range(part_leng):
                prev = curr
                curr = curr.next

            if prev:
                prev.next = None

        return result
