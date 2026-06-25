class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a = 1
        b = 2
        for _ in range(n-2):
            c = a + b
            a = b
            b = c
        return b