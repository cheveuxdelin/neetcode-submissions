# say the problem in my own words
# discuss assumptions & constraints
# discuss edge & corner cases
# high level approach and why
# test case I come up myself
# does this make sense?
# code and explain
# dry run again
# complexity
# succeed


# theres always 1 island
# valid input
# an out of bounds would be counting towareds perimieter

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        water = 0
        land = 1
        visited = -1
        n = len(grid)
        m = len(grid[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m


        def dfs(i: int, j: int) -> int:
            grid[i][j] = visited
            count = 0
            for di, dj in directions:
                ii = i+di
                jj = j+dj
                if not in_bounds(ii, jj) or grid[ii][jj] == water:
                    count += 1
                elif grid[ii][jj] == land:
                    count += dfs(ii, jj)
            return count

        for i in range(n):
            for j in range(m):
                # we found the island!
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0