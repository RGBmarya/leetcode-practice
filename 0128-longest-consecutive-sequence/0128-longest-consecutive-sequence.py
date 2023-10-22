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

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(list(set(nums)))
        max_streak, cur_streak = 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur_streak += 1
            else:
                if cur_streak > max_streak:
                    max_streak = cur_streak
                cur_streak = 1
        if cur_streak > max_streak:
            max_streak = cur_streak
        return max_streak