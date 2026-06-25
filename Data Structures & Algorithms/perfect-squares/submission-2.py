class Solution:
    def numSquares(self, n: int) -> int:
        dp = [sys.maxsize] * (n+1)
        dp[0] = 0

        for target in range(1, n+1):
            i = 1
            while (candidate := i*i) <= target:
                dp[target] = min(dp[target], 1+dp[target-candidate])
                i += 1
        return dp[-1]