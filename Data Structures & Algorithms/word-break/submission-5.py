import functools

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # f(i) = can s be segmented starting from the ith index
        @functools.cache
        def f(i):
            if i == len(s):
                return True
            else:
                possible = False
                for word in wordDict:
                    if i+len(word) <= len(s) and s[i:i+len(word)] == word:
                        if f(i+len(word)):
                            possible = True
                            break
                return possible
        return f(0)
                    