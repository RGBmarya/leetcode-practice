"""
Plan
- maximize --> optimize: sliding window problem
- two pointers, slow and fast
- profit at any point = prices[fast] - prices[slow]
- increment the fast pointer over the entire list, keeping track of the index where the profit was maximized
- fixing the fast pointer at this index, increment the slow index, keeping track of where the profit was maximized
- return the different prices[fast] - prices[slow], or 0 if its negative


"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res