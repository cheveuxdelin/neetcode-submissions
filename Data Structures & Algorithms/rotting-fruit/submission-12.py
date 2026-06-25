class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        empty = 0
        fresh = 1
        rotten = 2
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        t = 0   
        q = deque()
        n_bananas = 0

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m
        
        for i in range(n):
            for j in range(m):
                n_bananas += grid[i][j] == rotten or grid[i][j] == fresh
                if grid[i][j] == rotten:
                    q.append((i, j))

        if n_bananas == len(q):
            return 0
        
        while q:
            for _ in range(len(q)):
                c_i, c_j = q.popleft()
                n_bananas -= 1
                for di, dj in directions:
                    ii = di+c_i
                    jj = dj+c_j
                    
                    if in_bounds(ii, jj) and grid[ii][jj] == fresh:
                        grid[ii][jj] = rotten
                        q.append((ii, jj))
            if q:
                t += 1
        return t if not n_bananas else -1
        

