import functools

class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort()
        n = len(envelopes)

        # dfs(i) = max additional chain length starting at i
        @functools.cache
        def dp(i: int) -> int:
            if i == n:
                return 0

            best = 1

            for j in range(i+1, n):
                if envelopes[i][0] < envelopes[j][0] and envelopes[i][1] < envelopes[j][1]:
                    best = max(best, 1 + dp(j))
            return best
        
        return max(dp(i) for i in range(n))

