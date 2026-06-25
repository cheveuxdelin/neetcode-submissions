class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 1
        rotten = 2
        n_fresh_fruits = 0
        queue = collections.deque()
        n_minutes = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == rotten:
                    queue.append((i, j))
                elif grid[i][j] == fresh:
                    n_fresh_fruits += 1

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        
        while queue:
            n_minutes += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j
                    if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and grid[ii][jj] == fresh:
                        grid[ii][jj] = rotten
                        n_fresh_fruits -= 1
                        if n_fresh_fruits == 0:
                            return n_minutes
                        queue.append((ii, jj)) 
        return -1 if n_fresh_fruits else 0