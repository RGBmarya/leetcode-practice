"""

Understand
    1
2       3
4 5     6 7

-> 4

Match
DFS

Plan
- diameter = max height of left subtree + max height of right subtree
- max height = 1 + max(left subtree, right subtree)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diam = 0
        def dfs(node):
            nonlocal max_diam
            
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            max_diam = max(max_diam, left + right)
            
            return 1 + max(left, right)
        dfs(root)
        return max_diam