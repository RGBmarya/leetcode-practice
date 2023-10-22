"""
Understand
[100, 4, 200, 1, 3, 2] --> len([1, 2, 3, 4]) = 4
[1, 2, 0, 1] --> 3
[] --> []

Plan

Evaluate
Time: O(nlogn + n) = O(nlogn)
Space: O(n)
"""

"""
Plan
- cannot sort - O(nlogn)
- iterate over the list
- check if there exists a streak ending with cur_num - 1; if so, append to that streak; else, create a new streak

{
[100]
[1, 2, 3, 4]
[200]
}

"""

class Solution:
#         if not nums:
#             return 0
        
#         nums = sorted(list(set(nums)))
#         max_streak, cur_streak = 1, 1
#         for i in range(1, len(nums)):
#             if nums[i] == nums[i - 1] + 1:
#                 cur_streak += 1
#             else:
#                 if cur_streak > max_streak:
#                     max_streak = cur_streak
#                 cur_streak = 1
#         if cur_streak > max_streak:
#             max_streak = cur_streak
#         return max_streak

    """
    Plan
    - convert nums into set to remove duplicates - O(1) lookup
    - for num in nums:
        - nums[i] is the start of a sequence if nums[i] - 1 is not in nums
        - if we encounter such a number, check if nums[i] + 1 is in list
        - if so, increment a counter
        - compare counter with max counter -> if greater, update max
        - repeat until nums[i] + 1 is not in list
    Evaluate
    Time: O(n) - visit each num at most twice
    
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_streak = 0
        for num in nums:
            if num - 1 not in nums_set:
                cur_streak = 1
                while num + cur_streak in nums_set:
                    cur_streak += 1
                if cur_streak > max_streak:
                    max_streak = cur_streak
        return max_streak