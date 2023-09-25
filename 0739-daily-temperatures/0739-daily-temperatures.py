"""
Understand

[50] --> [0]

Match

Plan
for each element, iterate forward until temp is higher than current temp while keeping track of the number of iterations (count)
- if you reach end of list, then count is set to 0
for each element at index i, update res[i] with number of iterations until warmer temperature

Evaluate
Time: O(n^2)
Space: O(1)
"""

class Solution:
    # def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #     res = [0] * len(temperatures)
    #     for i, t in enumerate(temperatures):
    #         count = 0
    #         while (i + count) < len(temperatures) and temperatures[i + count] <= t:
    #             count += 1
    #         if i + count == len(temperatures):
    #             count = 0
    #         res[i] = count
    #     return res
    
    """
    Plan
    - stack
    - iterate over the entire list
    - append (current element, index) to the stack
    - iterate + increment counter
    - while current element > element on top of the stack, remove element from the stack and update res[index] with (current index - index)
    - in any case, append (current element, index) to the top of the stack
    
    Evaluate
    Time: O(n + n) --> O(n)
    Space: O(n)
    """
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                prev_temp, temp_index = stack.pop()
                res[temp_index] = i - temp_index
            stack.append((temp, i))
        
        while stack:
            removed = stack.pop()
            res[removed[1]] = 0
        
        return res
    