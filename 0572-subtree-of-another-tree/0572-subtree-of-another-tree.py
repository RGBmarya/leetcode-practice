"""
Understand
Determine whether subtree exists within tree

Match
DFS

Plan

- know how to determine if two trees are identical
sameTree
    base cases:
        if both nodes are null, return True (reached leaves)
        if one of two nodes is null, return False
        if values of two nodes differ, return False
    recursive case:
        left children are equal AND right children are equal
        
        
        
isSubtree
- if subTree is empty, then subTree MUST be a subtree of tree (leaves of tree point to None)
- if subTree is non-empty and tree is empty, then subTree CANNOT be subtree of tree
- if root == subRoot (areIdentical), return True; else, check left and right children


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.areIdentical(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def areIdentical(self, root1, root2):
        if not root1 and not root2:
            return True
        if (not root1 or not root2) or (root1.val != root2.val):
            return False
        return self.areIdentical(root1.left, root2.left) and self.areIdentical(root1.right, root2.right)