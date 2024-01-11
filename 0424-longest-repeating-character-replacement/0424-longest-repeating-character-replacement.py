"""
Understand
asdf
A, 1 --> 1
AB, 1 --> 2
ABC, 2 --> 3
AABA, 1 --> 4

Match
Sliding window

Plan
- left, right pointers start at first char
- while right pointer is valid:
    - increment right pointer while keeping track of frq of chars in substring
    - if len(substring) - frq of most common > k (i.e., cannot replace all non-most common chars), increment left ptr, decrement count of left char
    - update max length of substring
    
Evaluate
Time: O(n * 26) = O(n)
Space: O(26)
    
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        maxLen = 0
        left = 0
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            
            if (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        return maxLen