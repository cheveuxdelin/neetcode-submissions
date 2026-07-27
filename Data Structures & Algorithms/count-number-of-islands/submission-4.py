# whenever we find a 1, we just dfs
# we spread 4 directionally
# we repeat the process on the whole grid

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
        ]
        n = len(grid)
        m = len(grid[0])

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        def helper(i: int, j: int):
            grid[i][j] = "0"
            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and grid[ii][jj] == "1":
                    helper(ii, jj)
            return 1

        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    result += helper(i, j)
        return result