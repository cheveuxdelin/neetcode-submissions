class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True


        def dfs(i, current):
            if i == len(s):
                result.append(current[:])
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    current.append(s[i:j+1])
                    dfs(j+1, current)
                    current.pop()
        dfs(0, [])
        return result
