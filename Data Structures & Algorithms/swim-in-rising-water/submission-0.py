class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        visited = set()
        heap = [(grid[0][0], 0, 0)]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        while heap:
            current_t, i, j = heapq.heappop(heap)
            if (i, j) not in visited:
                if (i, j) == (n-1, m-1):
                    return current_t
                else:
                    visited.add((i, j))
                    for di, dj in directions:
                        ii = i+di
                        jj = j+dj
                        if in_bounds(ii, jj) and (ii, jj) not in visited:
                            heapq.heappush(heap, (max(current_t, grid[ii][jj]), ii, jj))
        return -1