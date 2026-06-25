class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])

        pacific = [[False] * m for _ in range(n)]
        atlantic = [[False] * m for _ in range(n)]

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]

        def dfs(i, j, p_or_a):
            p_or_a[i][j] = True
            for di, dj in directions:
                ii = i+di
                jj = j+dj
                if 0 <= ii < n and 0 <= jj < m and heights[i][j] <= heights[ii][jj] and not p_or_a[ii][jj]:
                    dfs(ii, jj, p_or_a)

        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m-1, atlantic)
        for j in range(m):
            dfs(0, j, pacific)
            dfs(n-1, j, atlantic)
        
        return [[i, j] for j in range(m) for i in range(n) if pacific[i][j] and atlantic[i][j]]