class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_i = 0
        max_j = 0

        def expand(i, j):
            nonlocal max_i
            nonlocal max_j
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i > max_j - max_i:
                    max_i = i
                    max_j = j    
                i -= 1
                j += 1

        for i in range(len(s)):
            expand(i, i)
            if i+1 < len(s):
                expand(i, i+1)

        return s[max_i:max_j+1]