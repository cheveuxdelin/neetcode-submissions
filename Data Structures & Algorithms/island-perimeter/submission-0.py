from functools import cache

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def in_bounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0]) 

        def f(i, j):
            if (i, j) in visited:
                return 0
            if not in_bounds(i, j) or grid[i][j] == 0:
                return 1
            
            visited.add((i, j))
            return f(i+1, j) + f(i-1, j) + f(i, j+1) + f(i, j-1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return f(i, j)
                
