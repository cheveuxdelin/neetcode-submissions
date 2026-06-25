from functools import cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        @cache
        def backtrack(i, j):
            if j == m:
                return 1
            elif i < n:
                skipping = backtrack(i+1, j)
                taking = 0
                if s[i] == t[j]:
                    taking = max(taking, backtrack(i+1, j+1))
                return skipping + taking
            else:
                return 0
        return backtrack(0, 0)