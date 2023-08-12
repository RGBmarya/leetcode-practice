"""
Understand
- balanced = height of right and left subtrees differ at most by 1

Match
Recursive DFS

Plan
- perform recursive DFS traversal to calculate max height of left, right subtrees
    base case: return 0 if node is None
    recursive case: if max height of left, right subtrees differs by more than 1, return false; else, return height of subtree
    return true
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (True, 0)
            left = dfs(root.left)
            right = dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            return (balanced, 1 + max(left[1], right[1]))
            
        return dfs(root)[0]