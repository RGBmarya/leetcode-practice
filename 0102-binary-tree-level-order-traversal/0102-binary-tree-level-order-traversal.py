from collections import deque, defaultdict

"""
Understand

Match
BFS

Plan
- hashmap (level --> list of nodes)
- create a deque (level, node)
- while q is not empty:
     - pop from left --> current node, level
     - add current value to hashmap[level]
     - add children of current node to the deque

Evaluate
- Time: O(N)
- Space: queue is largest at last level (~N/2 nodes) --> O(N/2) = O(N)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return []
    
#         hashmap = defaultdict(list)
#         queue = deque()
#         queue.append((0, root))
#         while queue:
#             cur_level, cur_node  = queue.popleft()
#             hashmap[cur_level].append(cur_node.val)
#             if cur_node.left:
#                 queue.append((cur_level + 1, cur_node.left))
#             if cur_node.right:
#                 queue.append((cur_level + 1, cur_node.right))
#         return hashmap.values()
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        if root:
            q.append(root)
        while q:
            level = []
            for i in range(len(q)): # only evaluates at creation of for loop 
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res
                
            