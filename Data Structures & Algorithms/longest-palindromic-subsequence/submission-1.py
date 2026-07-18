import functools

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        result = 0
        @functools.cache
        def dfs(i, j):
            if i < 0 or j == len(s):
                return 0
            if s[i] == s[j]:
                length = 1 if i == j else 2
                length += dfs(i-1, j+1)
                return length
            else:
                return max(dfs(i-1, j), dfs(i, j+1))
        
        for i in range(len(s)):
            result = max(result, dfs(i, i), dfs(i, i+1))
        return result