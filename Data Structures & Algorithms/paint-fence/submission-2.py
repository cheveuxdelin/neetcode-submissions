import functools

class Solution:
    def numWays(self, n: int, k: int) -> int:
        @functools.cache
        def dp(i: int, previous_count: int):
            if i == n:
                return 1

            result = (k-1) * dp(i+1, 1)

            if previous_count < 2:
                result += dp(i+1, previous_count+1)
            return result
        return dp(0, 0)
                
