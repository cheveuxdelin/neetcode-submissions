class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        heap = [(grid[0][0], 0, 0)]
        directions = [
            (0, 1),
            (0,-1),
            (1, 0),
            (-1,0),
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m
        
        while True:
            current_t, c_i, c_j = heapq.heappop(heap)
            if (c_i, c_j) not in visited:
                visited.add((c_i, c_j))
                if (c_i, c_j) == (n-1, m-1):
                    return current_t
                for di, dj in directions:
                    ii = di+c_i
                    jj = dj+c_j
                    if in_bounds(ii, jj) and (ii, jj) not in visited:
                        heapq.heappush(heap, (max(current_t, grid[ii][jj]), ii, jj))