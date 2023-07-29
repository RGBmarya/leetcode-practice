
"""
Understand

car, rat -> False

anagram, nagaram -> True

Match
hashmap

Plan
- create hashmap for each word (letter: frq)
- compare hashmaps

Evaluate 
Time: O(s + t)
Space: O(s + t)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash, t_hash = {}, {}
        for l in s:
            s_hash[l] = 1 + s_hash.get(l, 0)
        for l in t:
            t_hash[l] = 1 + t_hash.get(l, 0)
        return s_hash == t_hash