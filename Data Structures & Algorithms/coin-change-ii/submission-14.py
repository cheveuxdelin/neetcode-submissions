import functools


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin_index in range(1, len(coins)+1):
            for current_amount in range(1, amount+1):
                if current_amount >= coins[coin_index-1]:
                    dp[current_amount] += dp[current_amount - coins[coin_index-1]]
        return dp[-1]

