import functools
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @functools.cache
        def dp(i: int, is_buying: bool) -> int:
            if i >= len(prices):
                return 0
            elif is_buying:
                return max(
                    dp(i+1, True),
                    -prices[i] + dp(i+1, False),
                )
            else:
                return max(
                    dp(i+1, False),
                    prices[i] + dp(i+2, True),
                )
        return dp(0, True)
