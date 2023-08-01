from collections import defaultdict

"""
Understand
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

[""]
-> [[""]]

["a"]
-> [["a"]]

Match
hashmap

Plan
- two words = anagrams IFF frequency of letters are same 
- hashmap (key = tuple, index corresponds to letter, value corresponds to frequency; value = list of anagrams) - tuples are hashable bc IMMUTABLE
- append to list if tuple matches key in hashmap, else create new k:v pair
- return hashmap.values()



"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagrams[tuple(count)].append(s)
        return anagrams.values()