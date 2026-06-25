
# n_chests >= 0
# a cell can stay untraversed
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        non_traversable = -1
        treasure = 0
        traversable = 2147483647

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        def dfs(i: int, j: int, n: int):
            # this would mark as visited
            # since we are checking against unvisited (traversable)
            grid[i][j] = n
            for di, dj in directions:
                ii = i+di
                jj = j+dj
                if in_bounds(ii, jj) and (grid[ii][jj] == traversable or n+1 <= grid[ii][jj]):
                    dfs(ii, jj, n+1)

        
        chests = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == treasure]
        for chest in chests:
            dfs(*chest, 0)