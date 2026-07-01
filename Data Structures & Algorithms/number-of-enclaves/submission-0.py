class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        directions = [
            (0, 1),
            (0,-1),
            (1, 0),
            (-1,0),
        ]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def helper(i, j):
            if in_bounds(i, j) and (i, j) not in visited and grid[i][j] == 1:
                grid[i][j] = 0
                visited.add((i, j))
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j
                    helper(ii, jj)

        for i in range(n):
            helper(i, 0)
            helper(i, m-1)
        for j in range(m):
            helper(0, j)
            helper(n-1, j)

        result = 0
        for i in range(n):
            for j in range(m):
                result += grid[i][j] == 1
        return result