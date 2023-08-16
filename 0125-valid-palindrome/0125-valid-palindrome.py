"""
Understand

Match

Plan
- filter out non-alphanumeric --> conver to a list
- 2 pointers, 1 at each end --> iterate inwards while comparing values
- if values differ, return False
- return True

Evaluate
Time: O(n + n) -> O(n)
Space: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        return True