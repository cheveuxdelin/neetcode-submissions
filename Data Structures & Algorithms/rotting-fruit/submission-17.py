class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        empty = 0
        fresh = 1
        rotten = 2

        directions = (
            (0,1),
            (0, -1),
            (1, 0),
            (-1, 0),
        )

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m
        
        current_day = []
        # need to count that we touched all bananas as to determine if we managed to rot them all
        number_of_bananas = 0
        time_elapsed = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == rotten:
                    current_day.append((i, j))
                if grid[i][j] != empty:
                    number_of_bananas += 1

        while current_day:
            next_day = []
            for i, j in current_day:
                number_of_bananas -= 1
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j
                    if in_bounds(ii, jj) and grid[ii][jj] == fresh:
                        grid[ii][jj] = rotten
                        next_day.append((ii, jj))
            current_day = next_day
            if current_day:
                time_elapsed += 1
        
        # we were able to process all bananas
        if number_of_bananas == 0:
            return time_elapsed
        else:
            return -1
            