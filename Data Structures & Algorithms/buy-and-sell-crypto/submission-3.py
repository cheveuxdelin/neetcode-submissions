class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        current_min = sys.maxsize

        for price in prices:
            current_min = min(current_min, price)
            total = max(total, price - current_min)
        return total