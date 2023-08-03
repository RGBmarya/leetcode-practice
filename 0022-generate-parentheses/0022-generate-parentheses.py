"""
Understand
(n-1)^2 + 1
n = 1
()

n = 2
()() (())

n = 3
((())), (()()), ()(()), (())(), ()()()

Plan
- add open parenthesis if open < n
- add closing parenthesis if close < open
- valid IFF open == closing == n
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        
        def generate(string):
            counts = {}
            for c in string:
                counts[c] = 1 + counts.get(c, 0)
                
            if counts.get("(", 0) == counts.get(")", 0) == n:
                res.append(string)
                return 
            if counts.get("(", 0) < n:
                generate(string + "(")
            if counts.get(")", 0) < counts.get("(", 0):
                generate(string + ")")
                
        generate("(")
        return res