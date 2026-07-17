class Solution:
    def tribonacci(self, n: int) -> int:
        if n  == 0:
            return 0
        if n < 3:
            return 1

        dp = [0,1,1]

        for _ in range(n-2):
            next_number = sum(dp)

            tmp = dp[-1]
            dp[-1] = next_number

            for i in range(len(dp)-2, -1, -1):
                tmp2 = dp[i]
                dp[i] = tmp
                tmp = tmp2
        return dp[-1]