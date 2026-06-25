class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""

        def expand(i, j):
            nonlocal result
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    if j-i+1 > len(result):
                        result = s[i:j+1]
                    i -= 1
                    j += 1
                else:
                    break

        for i in range(len(s)):
            expand(i, i)
            if i < len(s)-1:
                expand(i, i+1)
        
        return result