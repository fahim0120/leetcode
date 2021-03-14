"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/symmetric-tree/
# Easy
# LinkedIn
# Most Liked
# Top Interviews


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        from collections import deque

        deq = deque()

        if root:
            deq.append(root.left)
            deq.append(root.right)

        while deq:
            t1 = deq.popleft()
            t2 = deq.popleft()

            if not t1 and not t2:
                continue

            if not t1 or not t2:
                return False

            if t1.val != t2.val:
                return False

            deq.append(t1.left)
            deq.append(t2.right)
            deq.append(t1.right)
            deq.append(t2.left)

        return True

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def helper(left: TreeNode, right: TreeNode) -> bool:
            if not left and not right:
                return True

            if not left or not right:
                return False

            check1 = helper(left.left, right.right)
            check2 = helper(left.right, right.left)
            return left.val == right.val and check1 and check2

        if not root:
            return True

        return helper(root.left, root.right)
'''
