"""
Understand
["2","1","+","3","*"]
(2 + 1) * 3 = 9

["4","13","5","/","+"]
(13 // 5) + 4 = 6

Match
Stack

Plan
- dummy result = 0
- iterate over the input array
    - each time we encounter an int, add to stack
    - each time we enounter an operator, perform operation using top two numbers on the stack --> pop two numbers
    - push the result to the stack
- return res[0]

Evaluate
Time: O(n)
Space: O(n)
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-*/"
        res = []
        for t in tokens:
            if t in operators:
                operand2 = res.pop()
                operand1 = res.pop()
                if t == "+":
                    res.append(operand1 + operand2)
                elif t == "-":
                    res.append(operand1 - operand2)
                elif t == "*":
                    res.append(operand1 * operand2) 
                else:
                    res.append(int(operand1 / operand2))
            else:
                res.append(int(t))
        return res[0]