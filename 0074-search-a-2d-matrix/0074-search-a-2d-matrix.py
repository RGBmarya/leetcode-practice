"""
Plan
- sorted --> BS
- 1st: which subarray does target lie in
- 2nd: BS within subarray to find target

Evaluate
Time: O(log m + log n) = O(log (m * n))
Space: O(1)
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        sub_index = 0;
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][0] > target:
                right = mid - 1
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                sub_index = mid;
                break;
        
        left, right = 0, len(matrix[sub_index]) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if matrix[sub_index][mid] > target:
                right = mid - 1
            elif matrix[sub_index][mid] < target:
                left = mid + 1
            else:
                return True
        
        return False