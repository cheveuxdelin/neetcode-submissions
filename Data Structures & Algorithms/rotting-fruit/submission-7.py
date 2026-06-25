# we start at minute 0
# no solution? return -1
# solution? return number of minutes
# if 0 fresh, >1 rotten? we return time_elapsed=0 (are we able to handle this implicityl?)
# what if n_fresh == 0?
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        empty = 0
        fresh = 1
        rotten = 2

        directions = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        queue = deque()
        n_fresh_left = 0
        time_elapsed = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == rotten:
                    queue.append((i, j))
                elif grid[i][j] == fresh:
                    n_fresh_left += 1
        
        if not n_fresh_left:
            return time_elapsed

        while queue:
            if n_fresh_left == 0:
                return time_elapsed

            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ii = i+di
                    jj = j+dj
                    if in_bounds(ii, jj) and grid[ii][jj] == fresh:
                        grid[ii][jj] = rotten
                        n_fresh_left -= 1
                        queue.append((ii, jj))
            time_elapsed += 1
        return -1