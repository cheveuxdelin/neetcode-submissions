class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = set()
        atlantic = set()

        directions = [
            (0, -1),
            (0, 1),
            (1, 0),
            (-1, 0)
        ]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j, current_set):
            current_set.add((i, j))
            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and (ii, jj) not in current_set and heights[ii][jj] >= heights[i][j]:
                    dfs(ii, jj, current_set)
        
        for column in range(m):
            dfs(0, column, pacific)
            dfs(n-1, column, atlantic)
        for row in range(n):
            dfs(row, 0, pacific)
            dfs(row, m-1, atlantic)
        
        return list(pacific.intersection(atlantic))