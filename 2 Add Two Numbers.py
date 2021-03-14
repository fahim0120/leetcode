"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/add-two-numbers/
# Medium
# Amazon
# Most Liked
# Top Interviews


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur1 = l1
        cur2 = l2
        res = ListNode()
        ans = res

        c = 0
        s = 0
        while cur1 and cur2:
            s = cur1.val + cur2.val + c
            c = s // 10

            ans.next = ListNode(s%10)
            ans = ans.next

            cur1 = cur1.next
            cur2 = cur2.next

        if not cur1 and cur2:
            self.addOneNumber(cur2, ans, c)
        elif cur1 and not cur2:
            self.addOneNumber(cur1, ans, c)
        elif not cur1 and not cur2 and c > 0:
            ans.next = ListNode(c)

        return res.next


    def addOneNumber(self, l: ListNode, ans: ListNode, c: int) -> None:
        while l:
            if c == 0:
                ans.next = l
                return

            s = l.val + c
            c = s // 10
            ans.next = ListNode(s%10)

            ans = ans.next
            l = l.next

        if c > 0:
            ans.next = ListNode(c)
