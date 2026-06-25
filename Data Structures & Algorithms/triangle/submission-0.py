class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]

        for i in reversed(range(len(triangle)-1)):
            next_dp = []
            for j in range(len(triangle[i])):
                next_dp.append(triangle[i][j] + min(
                    dp[j],
                    dp[j+1],
                ))
            dp = next_dp
        return dp[0]