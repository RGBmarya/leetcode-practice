"""
Understand
- get len of longest substring without repeating chars
"pmwek" --> 3
"dvdf" --> 3

Match
- sliding window

Plan
- left, right pointer - start and end of window --> start off at 0
- while right pointer < len(string)
    - expand right side of window until you encounter a letter that you have encountered before
    - keep track of this length (update maxLen variable)
    - contract left side of window until the duplicate letter is removed 
    - return to top

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left, right = 0, 0
        encountered = set()
        while right < len(s):
            if s[right] in encountered:
                print(encountered)
                maxLen = max(maxLen, right - left)
                while s[left] != s[right]:
                    encountered.remove(s[left])
                    left += 1
                left += 1
                
            encountered.add(s[right])
            right += 1      
        maxLen = max(maxLen, right - left)
        return maxLen