import functools


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins)+1)]
        for i in range(len(dp)):
            dp[i][0] = 1
        
        for i in range(1, len(dp)):
            for j in range(1, amount+1):
                # skip
                dp[i][j] = dp[i-1][j]
                # take
                if coins[i-1] <= j:
                    dp[i][j] += dp[i][j-coins[i-1]]
        return dp[-1][-1]

