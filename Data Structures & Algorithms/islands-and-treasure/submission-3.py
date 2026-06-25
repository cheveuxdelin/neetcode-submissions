class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        land = 2147483647
        chest = 0
        water = -1
        
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and grid[ii][jj] != water and grid[i][j]+1 <= grid[ii][jj]:
                    grid[ii][jj] = grid[i][j]+1
                    dfs(ii, jj)

        chests = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == chest:
                    chests.append((i, j))

        for i, j in chests:
            dfs(i, j)