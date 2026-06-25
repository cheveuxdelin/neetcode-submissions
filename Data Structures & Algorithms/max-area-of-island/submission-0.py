class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def check_bounds(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def dfs(i, j):
            if not check_bounds(i, j):
                return 0
            
            if grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            return 0

        max_area = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                max_area = max(max_area, dfs(i, j))
        return max_area