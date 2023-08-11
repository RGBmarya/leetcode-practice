from collections import deque

"""
Match
BFS

Plan
- queue
- append new node 
- popleft, swap left and right nodes if not None
- append new left node and right node to the queue
- repeat until queue is empty 

Evaluate
Time: O(n)
Space: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        while len(q) > 0:
            node = q.popleft()
            if node: 
                temp = node.left
                node.left = node.right
                node.right = temp

                q.append(node.left)
                q.append(node.right)
        return root