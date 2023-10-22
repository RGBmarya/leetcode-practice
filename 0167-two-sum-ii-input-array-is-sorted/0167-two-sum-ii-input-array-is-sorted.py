"""
Plan
naive
- for each number, iterate over the succeeding numbers and check if sum = target; if so, return [index + 1, index2 + 1]
- if sum exceeds the target, move the next num

binary search
- for each number, calculate the complement = target - num
- perform binary search to get index of complement
- if complement does not exist, move to next num; else, return [index + 1, complement_index + 1]


Evaluate:
Time: < O(n^2)
Space: O(1)
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i + 1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return [i + 1, j + 1]
        #         if numbers[i] + numbers[j] > target:
        #             break
        
        for i in range(len(numbers)):
            complement = target - numbers[i]
            # if complement > numbers[i]:
            #     left = i + 1
            #     right = len(numbers) - 1
            # elif complement < numbers[i]:
            if complement == numbers[i]:
                return [i + 1, i + 2]
            left = 0
            right = len(numbers) - 1

            
            while left <= right:
                middle = (left + right) // 2
                if numbers[middle] == complement and i != middle:
                    return [i + 1, middle + 1]
                elif numbers[middle] > complement:
                    right = middle - 1
                else:
                    left = middle + 1