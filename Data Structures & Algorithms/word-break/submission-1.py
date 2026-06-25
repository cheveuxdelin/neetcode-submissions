from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # depends on back states
        @cache
        def backtrack(i):
            if i == len(s):
                return True
            elif i < len(s):
                for word in wordDict:
                    if s[i:i+len(word)] == word and backtrack(i+len(word)):
                        return True
            return False
        return backtrack(0)
                        