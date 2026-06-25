class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def expand(i, j):
            nonlocal result
            while i >= 0 and j < len(s) and s[i] == s[j]:
                result += 1
                i -= 1
                j += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        return result