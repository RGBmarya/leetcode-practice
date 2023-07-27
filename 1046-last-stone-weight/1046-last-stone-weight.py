import heapq
"""
Understand
[1, 2, 3, 4]
-> [1, 2, 1]
-> [1, 1]
-> [0]
-> 0


[1, 2, 3, 5]
-> [1, 2, 2]
-> [1]
-> 1

[1, 2, 3, 6]
-> [1, 2, 3]
-> [1, 1]
-> [0]
-> 0

Match
recursion + heap

Plan
- base case: list has 1 element (return element) or 0 elements (return 0)
- recursive case:
    - get highest two values (max heap, pop twice)
    - calculate and add diff to heap if diff != 0
    - call function with new stones list
"""

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-1 * x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            if (abs(stone1-stone2)) != 0:
                heapq.heappush(stones, abs(stone1-stone2) * -1)
        if stones:
            return stones[0] * -1
        return 0