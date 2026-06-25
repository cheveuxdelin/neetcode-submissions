import functools
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)
        m = len(word2)
        dp = [j for j in range(m+1)]

        for i in range(1, n+1):
            last_diagonal = dp[0]
            dp[0] = i
            for j in range(1, m+1):
                tmp = dp[j]
                if word1[i-1] != word2[j-1]:
                    dp[j] = 1 + min(
                        dp[j],
                        dp[j-1],
                        last_diagonal,
                    )
                else:
                    dp[j] = last_diagonal
                last_diagonal = tmp
        return dp[-1]