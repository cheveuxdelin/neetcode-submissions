# say the problem in my own words
# clarify input constraints and assumptions
# discuss corner and edge cases
# high level approach and why
# dry test cases
# DOES THIS MAKE SENSE?
# code and explain
# dry test again
# SUCCESS


# valid inputs (n > 0, m > 0)
# only 1s and 0s
# number of islands >= 0
# good algorithm to handle big size
# can mutate array
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        water = 0
        land = 1
        n = len(grid)
        m = len(grid[0])
        result = 0
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        def dfs(i: int, j: int) -> int:
            # marking as visited
            grid[i][j] = water
            # counting also self
            result = 1
            # for each neighbor
            for di, dj in directions:
                ii = i+di
                jj = j+dj
                # land being not visited, since we mark visited as water
                if in_bounds(ii, jj) and grid[ii][jj] == land:
                    result += dfs(ii, jj)
            return result


        for i in range(n):
            for j in range(m):
                if grid[i][j] == land:
                    result = max(result, dfs(i, j))
        return result