import heapq

"""
Understand

[1, 1, 1, 2, 2, 3], k = 2
-> [1, 2]

[1, 2, 2, 3], k = 1
-> [2]

[1] k = 1
-> [1]

Match
Hashmap + heap

Plan
- hashmap (element : frq)
- iterate over the list to update frequencies in hashmap - O(n)
- hashmap -> max heap with key = frq -> pop k times to return top k most frequent elements

Evaluate
Time: O(n) + O(n) + O(n) + O(k) -> O(n)
Space: O(n) + O(n) -> O(n)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        max_heap = [(f * -1, num) for num, f in counts.items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for i in range(k)]