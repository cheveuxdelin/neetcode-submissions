
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        current_min = prices[0]
        max_profit = 0
        
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
        return max_profit