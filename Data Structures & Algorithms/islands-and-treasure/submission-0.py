class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]
        n_rows = len(grid)
        n_cols = len(grid[0])

        def f(i, j, current_distance):
            if current_distance <= grid[i][j]:
                grid[i][j] = current_distance
                for direction in directions:
                    ii = i + direction[0]
                    jj = j + direction[1]
                    if 0 <= ii < n_rows and 0 <= jj < n_cols:
                        f(ii, jj, current_distance + 1)

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 0:
                    f(i, j, 0)
        
        