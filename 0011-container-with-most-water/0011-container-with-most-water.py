"""
Understand:

Match: 

Plan
- two pointers, left = 0, right = 1
- keep track of max area so far
- nested for loops
    - area = (right - left) * min(height[left], height[right])
    - update max if new area is larger
    - move to next combination

Evaluate: 
- time: O(n^2)
- space: O(1)


--------------
Understand: 

[2, 8, 1] --> 2
[2, 8, 10] --> 8

Match: two-pointer

Plan: 
- left start at the beginning, right at end 
- while left pointer < right
    - compute area = (right - left) * min(height[left], height[right]) and update max
    - if height of left < height of right, shift left to right
    - any other case, shift right one to left

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        curMax = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            curMax = max(area, curMax)
            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1
        return curMax