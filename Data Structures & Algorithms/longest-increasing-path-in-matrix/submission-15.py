class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(100000)
        n = len(matrix)
        m = len(matrix[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m
        
        dp = [[0] * m for _ in range(n)]
        # we needed a visited, since we could do a circle/loop
        # actually, something must be wrong in the logic
        # since we always increase, we should never be going back to a already visited node
        # since its going to be smaller than current

        def dfs(i: int, j: int):
            if dp[i][j]:
                return dp[i][j]
            
            best = 1
            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and matrix[ii][jj] > matrix[i][j]:
                    best = max(best, 1 + dfs(ii, jj))
            dp[i][j] = best
            return best
        
        result = 0

        for i in range(n):
            for j in range(m):
                result = max(result, dfs(i, j))
        return result
        