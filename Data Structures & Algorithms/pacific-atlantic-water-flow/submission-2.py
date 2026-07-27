# its about, for a given cell, if theres a 4-way path to both oceans
# if we start from the shore of each ocean, we can dfs into finding
# all cells that are reachable from those
# and we find the intersection of both sets
# dfs
# 2 grids for visited

# we need to check for visited
# since it could get stuck on equal height cells
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        def dfs(i: int, j: int, visited: list[list[bool]]):
            visited[i][j] = True
            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and heights[ii][jj] >= heights[i][j] and not visited[ii][jj]:
                    dfs(ii, jj, visited)

        pacific_visited = [[False] * m for _ in range(n)]
        atlantic_visited = [[False] * m for _ in range(n)]

        for i in range(n):
            dfs(i, 0, pacific_visited)
            dfs(i, m-1, atlantic_visited)
        for j in range(m):
            dfs(0, j, pacific_visited)
            dfs(n-1, j, atlantic_visited)
        return [[i, j] for i in range(n) for j in range(m) if pacific_visited[i][j] and atlantic_visited[i][j]]
