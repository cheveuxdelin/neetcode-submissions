class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n = len(grid)
        m = len(grid[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m
        
        def dfs(i, j):
            area = 1
            grid[i][j] = 0
            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and grid[ii][jj] == 1:
                    area += dfs(ii, jj)
            return area
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area