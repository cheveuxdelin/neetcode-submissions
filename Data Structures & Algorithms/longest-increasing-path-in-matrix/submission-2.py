class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(matrix), len(matrix[0])

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            visited.add((i, j))
            rest_of_path = 0
            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and (ii, jj) not in visited and matrix[i][j] < matrix[ii][jj]:
                    rest_of_path = max(rest_of_path, dfs(ii, jj))
            visited.discard((i, j))
            return 1 + rest_of_path
        
        return max(dfs(i, j) for i in range(n) for j in range(m))