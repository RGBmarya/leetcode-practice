import heapq

"""
Understand
[3, 4, 5, 6], k = 2
-> 5

[2, 1, 9, 4], k = 4
-> 1

[1, 1, 6, 6, 7, 9, 9, 9], k = 3
-> 9

Match
hashset + heap

Plan
- list -> max heap
- pop max heap k times to determine kth largest element

Evaluate
Time: O(n + k*logn) -> O(klogn)
Space: O(n)
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [num * -1 for num in nums]
        heapq.heapify(max_heap)
        for i in range(1, k + 1):
            e = heapq.heappop(max_heap)
            if i == k:
                return e * -1
    
# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution2:
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]