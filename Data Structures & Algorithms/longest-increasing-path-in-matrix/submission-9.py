class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
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

        indegrees = [[0] * m for _ in range(n)]
        queue = collections.deque()
        
        for i in range(n):
            for j in range(m):
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j
                    if in_bounds(ii, jj) and matrix[ii][jj] < matrix[i][j]:
                        indegrees[i][j] += 1
                if not indegrees[i][j]:
                    queue.append((i, j))
        
        result = 0

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j
                    if in_bounds(ii, jj) and matrix[ii][jj] > matrix[i][j]:
                        indegrees[ii][jj] -= 1
                        if not indegrees[ii][jj]:
                            queue.append((ii, jj))
            result += 1
        return result