class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0

        def check_boundary(i, j):
            return 0 <= i < len(grid) and 0 <= j < len(grid[0])

        def dfs(i, j):
            if not check_boundary(i, j):
                return 0

            if grid[i][j] == "1":
                grid[i][j] = 0
                dfs(i+1, j)
                dfs(i-1, j)
                dfs(i, j+1)
                dfs(i, j-1)
                return 1
            return 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += dfs(i, j)
        return total
