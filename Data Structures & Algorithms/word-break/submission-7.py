import functools

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp(i) = starting from index i, whether we can split s using wordDict
        @functools.cache
        def dp(i: int) -> bool:
            if i == len(s):
                return True
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word and dp(i+len(word)):
                    return True
            return False
        return dp(0)