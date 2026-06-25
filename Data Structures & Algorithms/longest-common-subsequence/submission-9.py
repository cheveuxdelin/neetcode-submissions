import functools

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp(i, j) longest common subsequence using text1[i:] and text2[j:]
        @functools.cache
        def dp(i, j):
            # nothing possible to match with an empty string
            if i == len(text1) or j == len(text2):
                return 0
            else:
                if text1[i] == text2[j]:
                    return 1 + dp(i+1, j+1)
                
                return max(
                    dp(i+1, j),
                    dp(i, j+1),
                )
        return dp(0, 0)
