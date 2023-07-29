from collections import defaultdict

"""
Understand

car, rat -> False

anagram, nagaram -> True

Match
hashmap

Plan
- create hashmap for each word (letter: frq)
- compare hashmaps
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)
        for l in s:
            s_hash[l] += 1
        for l in t:
            t_hash[l] += 1
        return s_hash == t_hash