from collections import deque

"""
Understand
Identical = same value, same order of nodes

Match
DFS

Plan
- each time a node is encountered, compare nodes at same position on both trees; 
- if both nodes are Null, return True (reached leaf on both trees, so equal)
- if one node Null and other not Null, return False
- if both nodes not Null AND diff values, return False
- return True
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p or not q) or (q.val != p.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)