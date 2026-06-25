import functools

class Solution:
    def climbStairs(self, n: int) -> int:
        
        @functools.cache
        def helper(n):
            if n <= 2:
                return n
            return helper(n-1) + helper(n-2)
        
        return helper(n)