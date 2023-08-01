import heapq

"""
Understand
[3, 4, 5, 6], k = 2
-> 5

[2, 1, 9, 4], k = 4
-> 1

[1, 1, 6, 6, 7, 9, 9, 9], k = 3
-> 9

Match
hashset + heap

Plan
- list -> max heap
- pop max heap k times to determine kth largest element

Evaluate
Time: O(n + k*logn) -> O(klogn)
Space: O(n)
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [num * -1 for num in nums]
        heapq.heapify(max_heap)
        for i in range(1, k + 1):
            e = heapq.heappop(max_heap)
            if i == k:
                return e * -1