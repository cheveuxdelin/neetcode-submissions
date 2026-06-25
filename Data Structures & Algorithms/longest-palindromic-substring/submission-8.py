class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = [-1, -1]

        def expand(i: int, j: int):
            nonlocal max_palindrome
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if j-i >= max_palindrome[1]-max_palindrome[0]:
                    max_palindrome = [i, j]
                i -= 1
                j += 1
        
        for i in range(len(s)):
            expand(i, i)
            if i < len(s)-1:
                expand(i, i+1)
        return s[max_palindrome[0]:max_palindrome[1]+1]
