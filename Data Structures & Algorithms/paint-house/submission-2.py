

class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        last_row = costs[0].copy()

        for i in range(1, len(costs)):
            next_row = [sys.maxsize] * 3
            for j in range(3):
                next_row[j] = costs[i][j] + min(
                    last_row[0] if j != 0 else sys.maxsize,
                    last_row[1] if j != 1 else sys.maxsize,
                    last_row[2] if j != 2 else sys.maxsize,
                )
            last_row = next_row
        return min(last_row)
