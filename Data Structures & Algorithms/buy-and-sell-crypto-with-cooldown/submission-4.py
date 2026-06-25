from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            skip = dfs(i+1, buying)

            if buying:
                return max(
                    dfs(i+1, not buying) - prices[i],
                    skip
                )
            else:
                return max(
                    dfs(i+2, not buying) + prices[i],
                    skip
                )
        return dfs(0, True)