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


"""

class Solution:
    """
    Evaluate
    Time: O(n + n + klogn) = O(klogn)
    Space: O(n) + O(n) -> O(n)
    """
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counts = {}
    #     for num in nums:
    #         counts[num] = 1 + counts.get(num, 0)
    #     max_heap = [(f * -1, num) for num, f in counts.items()]
    #     heapq.heapify(max_heap)
    #     return [heapq.heappop(max_heap)[1] for i in range(k)]
    
    """
    Evaluate
    Time: O(n)
    
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res