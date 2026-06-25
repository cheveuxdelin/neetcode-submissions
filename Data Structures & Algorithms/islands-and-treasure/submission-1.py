class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1),
        ]

        def f(i, j, current_distance):
            if current_distance <= grid[i][j]:
                grid[i][j] = current_distance
                for di, dj in directions:
                    ii, jj = i+di, j+dj
                    if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]):
                        f(ii, jj, current_distance+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    f(i, j, 0)