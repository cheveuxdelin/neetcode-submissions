import sys
import functools
sys.setrecursionlimit(10**7)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        directions = [
            (0, 1),
            (0,-1),
            (1, 0),
            (-1, 0),
        ]

        def in_bounds(i: int, j: int):
            return 0 <= i < n and 0 <= j < m

        @functools.cache
        def dp(i: int, j: int) -> int:
            best = 1

            for di, dj in directions:
                ii = di+i
                jj = dj+j

                if in_bounds(ii, jj) and matrix[ii][jj] > matrix[i][j]:
                    best = max(best, 1 + dp(ii, jj))
            return best

        return max(dp(i, j) for i in range(n) for j in range(m))