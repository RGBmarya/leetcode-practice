"""
BUY LOW, SELL HIGH
Understand: [7, 9, 2, 3, 6]

Match: sliding window

Plan:
- left, right = 0, 1
- keep track of max profit, profit = prices[right] - prices[left]
– update max
- calculate profit - if negative, shift both pointers; else, just shift right pointer

Evaluate
Time: O(n)
Space: O(1)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                curP = prices[right] - prices[left]
                maxP = max(curP, maxP)
            else:                
                left = right
            right += 1
        return maxP