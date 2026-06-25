class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [sys.maxsize] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if (candidate := i-coin) >= 0:
                    dp[i] = min(dp[i], 1+dp[candidate])
                else:
                    break
        return dp[-1] if dp[-1] != sys.maxsize else -1