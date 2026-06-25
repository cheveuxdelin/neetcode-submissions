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

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i, j))
        
        distance = 0

        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = distance

                for di, dj in directions:
                    ii = di+i
                    jj = dj+j

                    if in_bounds(ii, jj) and grid[ii][jj] != -1 and grid[ii][jj] == 2147483647:
                        grid[ii][jj] = 0
                        q.append((ii, jj))
            distance += 1
            
                

