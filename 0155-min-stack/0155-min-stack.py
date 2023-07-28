"""
Understand

stack.push(3) --> [3]
stack.push(4) --> [3, 4]
stack.pop() --> [3]
stack.top() --> 3
stack.getMin() --> 3

Match

Plan
Approach - store stack as a list, store min element separately
- push: O(1)
- pop: O(1)
- top: O(1)
- getMin: O(1)

Approach - store stack as a minheap, a most recent element separately
- push: O(logn)
- pop: O(logn)
- top: O(1)
- getMin: O(1)

"""

class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []
        
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.min_stack) == 0 or val < self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]        
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()