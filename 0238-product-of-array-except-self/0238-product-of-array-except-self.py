"""
Understand

[1, 2, 3, 4] 
-> [24, 12, 8, 6]

[1, 0, 3, 4, 5]
-> [0, 60, 0, 0, 0]

[3, 6]
-> [6, 3]

Match

Plan
- product at each index is equal to the product of numbers on either side
- two pass:
    - 1st pass: create list of prefix products, where res[i] is prefix for nums[i] (default prefix = 1)
    - 2nd pass: multiply prefixes at each index of res by postfix for nums[i] (default postfix = 1)
- return result

nums = [1, 2, 3, 4]
first pass = [1, 1, 2, 6]
second pass = [24, 12, 8, 6]
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
            