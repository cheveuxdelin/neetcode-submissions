import functools

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        dp = [0] * (m+1)

        for i in range(1, n+1):
            last_diagonal = 0

            for j in range(1, m+1):
                tmp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = 1 + last_diagonal
                else:
                    dp[j] = max(dp[j], dp[j-1])
                last_diagonal = tmp
        return dp[-1]


