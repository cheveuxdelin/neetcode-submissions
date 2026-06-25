class Solution:
    def longestPalindrome(self, s: str) -> str:
        result_i = 0
        result_j = 0

        def expand(i, j):
            nonlocal result_i
            nonlocal result_j
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j - i > result_j - result_i:
                    result_i = i
                    result_j = j
                i -= 1
                j += 1
        
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        
        return s[result_i:result_j+1]