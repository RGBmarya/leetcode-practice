"""
Understand
n == 2^x

Match
recursion

Plan
base - if n == 1, return True; elif n < 1, return False
recursive case: func(n / 2)

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n % 2 != 0 or n < 1:
            return False
        
        return self.isPowerOfTwo(n / 2)