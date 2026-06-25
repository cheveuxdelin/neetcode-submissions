class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        q = deque()
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m
        
        q = collections.deque()
        iteration_number = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        while q:
            for _ in range(len(q)):
                c_i, c_j = q.popleft()
                if grid[c_i][c_j] == 2147483647 or grid[c_i][c_j] == 0: # unvisited
                    grid[c_i][c_j] = iteration_number
                    for di, dj in directions:
                        ii = di+c_i
                        jj = dj+c_j
                        if in_bounds(ii, jj) and grid[ii][jj] == 2147483647:
                            q.append((ii, jj))
            iteration_number += 1

