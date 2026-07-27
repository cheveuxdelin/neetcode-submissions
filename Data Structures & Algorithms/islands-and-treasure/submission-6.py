# standard multi source bfs
# nothing crazy left to say
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        WATER = -1
        TREASURE = 0
        PATH = 2147483647

        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        stack = collections.deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == TREASURE:
                    stack.append((0, i, j))

        while stack:
            distance, i, j = stack.popleft()

            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and grid[ii][jj] == PATH:
                    grid[ii][jj] = distance + 1
                    stack.append((distance+1, ii, jj))