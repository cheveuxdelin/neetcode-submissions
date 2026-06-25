import functools

class Solution:
    def numWays(self, n: int, k: int) -> int:
        @functools.cache
        def dp(i: int):
            if i == n-1:
                return k
            if i == n-2:
                return k*k

            result = (k-1) * (dp(i+1) + dp(i+2))

            return result
        return dp(0)
                
