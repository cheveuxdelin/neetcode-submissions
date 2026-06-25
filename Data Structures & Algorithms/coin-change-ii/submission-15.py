import functools


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for current_amount in range(1, amount+1):
                if current_amount >= coin:
                    dp[current_amount] += dp[current_amount - coin]
        return dp[-1]

