"""
Understand
- get len of longest substring without repeating chars
"pmwek" --> 3
"dvdf" --> 3

Match
- sliding window

Plan
- left, right pointer - start and end of window --> start off at 0
expand right side of window until you encounter a letter that is in the substring...
- while right pointer < len(string)
    - if rightmost char is substring, contract left side of window until duplicate letter is removed
    - add rightmost char to set of chars in substring
    - update max length
    - increment right pointer

Evaluate
Time: O(n)
Space: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left, right = 0, 0
        substr_chars = set()
        while right < len(s):
            while s[right] in substr_chars:
                substr_chars.remove(s[left])
                left += 1
            substr_chars.add(s[right])
            res = max(res, len(substr_chars))
            right += 1
        return res