class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

        def helper(i: int):
            if i == len(s):
                result.append(current.copy())
            else:
                for j in range(i, len(s)):
                    if dp[i][j]:
                        current.append(s[i:j+1])
                        helper(j+1)
                        current.pop()
        helper(0)
        return result
            