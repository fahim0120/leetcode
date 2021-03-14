"""
 fahim0120@gmail.com
"""

# https://leetcode.com/problems/serialize-and-deserialize-bst/
# Medium

# Tree
# Preorder traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def helper(root: TreeNode) -> str:
            """
            Preorder traversal (leaves replaced with 'X') -> join with commas
            """
            if not root:
                return 'X'

            return f'{str(root.val)},{helper(root.left)},{helper(root.right)}'

        return helper(root)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(data: list) -> TreeNode:
            """
            Reverse of the other one.
            'X' found -> backtrack.
            """
            value = data.popleft()
            if value == 'X':
                return None

            node = TreeNode(value)
            node.left = helper(data)
            node.right = helper(data)

            return node

        return helper(deque(data.split(',')))



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
