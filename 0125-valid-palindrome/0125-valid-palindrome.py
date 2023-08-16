"""
Understand

Match

Plan
- filter out non-alphanumeric --> conver to a list
- 2 pointers, 1 at each end --> iterate inwards while comparing values
- if values differ, return False
- return True
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lst = [c for c in s if c.isalnum()]
        l, r = 0, len(lst) - 1
        while l <= r:
            if lst[l] != lst[r]:
                return False
            l += 1
            r -= 1
        return True