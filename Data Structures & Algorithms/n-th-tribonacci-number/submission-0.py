class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            a = 0
            b = 1
            c = 1
            for _ in range(n-2):
                tmp = a+b+c
                a = b
                b = c
                c = tmp
            return c