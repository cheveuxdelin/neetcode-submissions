# unlimited amounts of each coin
# each coin unique
# no negative coins
from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]

        for i in range(len(coins)+1):
            dp[i][0] = 1
        
        for coin_index in range(1, len(coins)+1):
            for current_amount in range(1, amount+1):
                # skip current coin
                dp[coin_index][current_amount] = dp[coin_index-1][current_amount]

                # use current coin
                if current_amount - coins[coin_index-1] >= 0:
                    dp[coin_index][current_amount] += dp[coin_index][current_amount - coins[coin_index-1]]
        return dp[-1][-1]