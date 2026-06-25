class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(i, j, skipped_already):
            while i < j:
                if s[i] != s[j]:
                    if skipped_already:
                        return False
                    return is_palindrome(i+1, j, True) or is_palindrome(i, j-1, True)
                i += 1
                j -= 1
            return True
        
        return is_palindrome(0, len(s)-1, False)