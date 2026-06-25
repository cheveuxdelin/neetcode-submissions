import functools

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @functools.cache
        def backtrack(i: int):
            if i >= len(cost):
                return 0
            return cost[i] + min(backtrack(i+2), backtrack(i+1))
        return min(backtrack(0), backtrack(1))