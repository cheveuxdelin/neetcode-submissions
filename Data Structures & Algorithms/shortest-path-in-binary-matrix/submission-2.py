class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        n = len(grid)
        m = len(grid[0])
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1 ),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m
        queue = deque([(0, 0)])
        length = 1

        while queue:
            for _ in range(len(queue)):
                c_i, c_j = queue.popleft()
                if (c_i, c_j) == (n-1, m-1):
                    return length
                grid[c_i][c_j] = 1
                for di, dj in directions:
                    ii = c_i+di
                    jj = c_j+dj
                    if in_bounds(ii, jj) and grid[ii][jj] == 0:
                        queue.append((ii, jj))
            length += 1
        return -1