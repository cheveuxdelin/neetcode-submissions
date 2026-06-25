class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        empty = 0
        fresh = 1
        rotten = 2
        fruit_count = 0
        queue = collections.deque()
        n_minutes = -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == rotten:
                    queue.append((i, j))
                if grid[i][j] != empty:
                    fruit_count += 1

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        if fruit_count == len(queue):
            return 0
        
        while queue:
            n_minutes += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                fruit_count -= 1
                for di, dj in directions:
                    ii, jj = i+di, j+dj
                    if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == fresh:
                        grid[ii][jj] = rotten
                        queue.append((ii, jj))

        return n_minutes if not fruit_count else -1