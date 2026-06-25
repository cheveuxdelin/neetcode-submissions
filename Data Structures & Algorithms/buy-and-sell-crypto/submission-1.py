class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_min = prices[0]
        result = 0

        for price in prices:
            current_min = min(current_min, price)
            result = max(result, price - current_min)
        
        return result