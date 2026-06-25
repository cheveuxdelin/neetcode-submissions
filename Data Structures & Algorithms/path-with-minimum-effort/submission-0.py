class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0),
        ]
        n = len(heights)
        m = len(heights[0])
        distances = [[sys.maxsize] * m for _ in range(n)]
        heap = [(0, 0, 0)]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        while heap:
            distance, i, j = heapq.heappop(heap)
            if distances[i][j] == sys.maxsize:
                distances[i][j] = distance
                if (i, j) == (n-1, m-1):
                    break
                for di, dj in directions:
                    ii = i+di
                    jj = j+dj
                    if in_bounds(ii, jj) and distances[ii][jj] == sys.maxsize:
                        effort = abs(heights[ii][jj] - heights[i][j])
                        heapq.heappush(heap, (max(distance, effort), ii, jj))
        return distances[-1][-1]
        