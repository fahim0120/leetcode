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
