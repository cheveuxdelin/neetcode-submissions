
class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        dp = [[sys.maxsize, sys.maxsize, sys.maxsize] for _ in range(len(costs))]

        dp[0] = costs[0].copy()

        for i in range(1, len(costs)):
            for j in range(3):
                dp[i][j] = costs[i][j] + min(
                    dp[i-1][0] if j != 0 else sys.maxsize,
                    dp[i-1][1] if j != 1 else sys.maxsize,
                    dp[i-1][2] if j != 2 else sys.maxsize,
                )
        return min(dp[-1])
