"""
Understand
() -> True

[]() -> True

[{()}] - True

[{]} - False

(] - False

{( - False

]} - False

Match
Stack + hashmap

Plan
- append opening brackets to stack
- if closing encoutered, check if closing bracket matches opening bracket at top of stack (use hashmap to compare expected opening bracket with top of stack)
- if match, pop stack; else, return false
- explanation: most recently encountered opening bracket must have the closest closing bracket

Evaluate
Time: O(n)
Space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            "}" : "{",
            "]" : "[",
            ")" : "(",
            
        }
        opening = []
        
        for char in s:
            if char in close_to_open.values():
                opening.append(char)
            elif opening and close_to_open[char] == opening[-1]:
                opening.pop()
            else:
                return False
        return not opening