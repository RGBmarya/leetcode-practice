import heapq
"""
Understand
[[1, 1], [2, 2], [3, 3]], k = 2:
[[1, 1], [2, 2]]

[[1, 1]], k = 1
[[1, 1]]

Match
Heap

Plan
- for each ordered pair, push to the min heap (key = euclidian distance from origin)
- pop first k element (k closest points) --> return a list of these points
"""

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        temp = [((math.sqrt(p[0]**2 + p[1]**2)), p) for p in points]
        heapq.heapify(temp)
        return [heapq.heappop(temp)[1] for i in range(k)]