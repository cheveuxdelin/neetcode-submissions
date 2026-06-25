import functools

class Solution:
    def integerBreak(self, n: int) -> int:
        @functools.cache
        def dp(current: int):
            best = current
            for i in range(1, current):
                best = max(best, i * dp(current-i))
            return best

        best = -1

        for i in range(1, n):
            best = max(best, i * dp(n-i))
        return best