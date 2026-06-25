class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        result = money - sum(prices[:2])
        if result >= 0:
            return result
        return money