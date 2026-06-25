import functools
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # previous: 0,1,2
        @functools.cache
        def dp(previous: int, i: int):
            if i == len(costs):
                return 0
            
            best = sys.maxsize
            for j in range(3):
                if j != previous:
                    best = min(best, costs[i][j] + dp(j, i+1))
            return best
        return dp(-1, 0)