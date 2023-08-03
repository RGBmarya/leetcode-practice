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
        stack = []
        res = []          
        
        def backtrack(nOpen, nClose):      
            if nOpen == nClose == n: 
                res.append("".join(stack))
                return
            if nOpen < n:
                stack.append("(")
                backtrack(nOpen + 1, nClose)
                stack.pop()
            if nClose < nOpen:
                stack.append(")")
                backtrack(nOpen, nClose + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res