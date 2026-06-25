class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        current = []

        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def helper(i):
            if i == len(s):
                result.append(current.copy())
            else:
                for j in range(i, len(s)):
                    if is_palindrome(i, j):
                        current.append(s[i:j+1])
                        helper(j+1)
                        current.pop()
        helper(0)
        return result