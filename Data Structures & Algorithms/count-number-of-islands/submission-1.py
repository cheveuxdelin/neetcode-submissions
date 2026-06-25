# state the problem in my own words
# clarify constraints and assumptinos
# edge and corner cases
# high level approach and why
# test cases on my own
# does this make sense?
# code and explain
# dry run again
# success

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        water = "0"
        land = "1"
        n = len(grid)
        m = len(grid[0])

        result = 0

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        def dfs(i: int, j: int) -> int:
            # mark as visited
            grid[i][j] = water
            for di, dj in directions:
                ii = i+di
                jj = j+dj
                if in_bounds(ii, jj) and grid[ii][jj] == land:
                    dfs(ii, jj)
            return 1

        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == land:
                    result += dfs(i, j)
        return result