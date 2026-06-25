class Solution:
    def climbStairs(self, n: int) -> int:
        # if n <=2, f(n) == n
        # f(n) = f(n-1) + f(n-2)

        if n <= 2:
            return n

        a = 1
        b = 2

        for _ in range(n-2):
            c = a + b
            a = b
            b = c
        return c