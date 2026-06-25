class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        def expand(i, j):
            nonlocal result
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    result += 1
                else:
                    break
                i -= 1
                j += 1
            return result
        
        for i in range(len(s)):
            expand(i, i)
            if i < len(s)-1:
                expand(i, i+1)
        return result