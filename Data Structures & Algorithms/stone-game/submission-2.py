from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def f(i, j):
            if i > j:
                return 0
            even = (j-i) % 2

            left = piles[i] if even else 0
            right = piles[j] if even else 0

            return max(
                left+f(i+1, j),
                right+f(i, j-1),
            )
        return f(0, len(piles)-1) > sum(piles) // 2