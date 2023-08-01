
class Solution(object):
    """
    time: O(n^2)
    space: O(1)
    """

    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """

    #     for i in range(len(nums)):
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] + nums[j] == target:
    #                 return [i, j]

    """
    time: O(n)
    space: O(n)
    """
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [i, hashmap.get(target - nums[i])]
            hashmap[nums[i]] = i
            