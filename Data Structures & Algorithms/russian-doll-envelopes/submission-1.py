import functools

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort()

        n = len(envelopes)
        dp = [1 for _ in range(n)]

        for i in reversed(range(n-1)):
            for j in range(i, n):
                if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
                    dp[i] = max(dp[i], 1 + dp[j])        
        return max(dp)
