import sys
import functools

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        
        for current_amount in range(1, amount+1):
            for coin in coins:
                if current_amount >= coin:
                    dp[current_amount] = min(dp[current_amount], 1 + dp[current_amount-coin])
        return dp[amount] if dp[amount] != sys.maxsize else -1
\