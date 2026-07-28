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
        
        # we want to count the indegrees for all
        indegrees = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j
                    if in_bounds(ii, jj) and matrix[i][j] < matrix[ii][jj]:
                        indegrees[ii][jj] += 1
        
        # lets find all the minimums
        current_layer = []

        for i in range(n):
            for j in range(m):
                if not indegrees[i][j]:
                    current_layer.append((i, j))
        
        n_layers = 0
        while current_layer:
            n_layers += 1
            next_layer = []

            for i, j in current_layer:
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j
                    if in_bounds(ii, jj) and matrix[i][j] < matrix[ii][jj]:
                        indegrees[ii][jj] -= 1
                        if indegrees[ii][jj] == 0:
                            next_layer.append((ii, jj))
            current_layer = next_layer
        return n_layers
