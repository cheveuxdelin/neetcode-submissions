import functools

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp(i, j): number of distinct subsequences of s, starting from i, equals to t[j:]
        @functools.cache
        def dp(i: int, j: int) -> int:
            # we were able to make it to the finish line for what's considered a subsequence
            if j == len(t):
                return 1
            # we ran out of search space
            if i == len(s):
                return 0
            # skip
            skipping = dp(i+1, j)
            # take
            taking = dp(i+1, j+1) if s[i] == t[j] else 0
            return skipping + taking
        return dp(0, 0)
                