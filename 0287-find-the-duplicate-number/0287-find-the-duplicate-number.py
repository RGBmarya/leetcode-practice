"""
Understand
[1, 1] --> 1
[2, 1, 3, 1] --> 1

Match
Hashmap

Plan
hashmap (num, frq)
iterate over the entire list, keeping track of frq of each element
return element with frq != 1 (max frq)
XXXX - Floyd's tortoise and hare algorithm --> eventually pointers will intersect, which can result in false positive 

Evalute
Time: O(n + n) --> O(n)
Space: O(n - 1) --> O(n)
"""

class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         counts = {}
#         for num in nums:
#             counts[num] = 1 + counts.get(num, 0)
#         return max(counts, key=lambda n: counts.get(n))

    """
    Plan
    iterate over list, keeping track of encountered elements in set
    if encountered, return cur element
    
    Evaluate
    Time: O(n)
    Space: O(n)
    """
    def findDuplicate(self, nums: List[int]) -> int:
        encountered = set()
        for num in nums:
            if num in encountered:
                return num
            encountered.add(num)
