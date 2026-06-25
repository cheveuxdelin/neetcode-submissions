import functools

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for coin in coins:
            for amount_to_build in range(coin, len(dp)):
                dp[amount_to_build] += dp[amount_to_build-coin]
        return dp[-1]