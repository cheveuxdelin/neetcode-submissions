import functools
class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.cache
        def dfs(i: int) -> int:
            if i >= len(s):
                return 1
            if s[i] == "0":
                return 0
            return dfs(i+1) + (dfs(i+2) if i < len(s)-1 and int(s[i:i+2]) <= 26 else 0)
        return dfs(0)
