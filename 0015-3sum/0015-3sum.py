"""
Plan

consider a sorted list
[-4, -1, -1, 0, 1, 2]
i = 0
complement = 0 - nums[left]
find two numbers in nums[left + 1:end] + nums[i] that sum to complement
append each combo to res
return res

Time: O(nlogn + n^2) = O(n^2)
Space: O(n) or O(1) depending on sorting
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res