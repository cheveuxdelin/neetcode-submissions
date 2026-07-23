class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
        ]
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        visited = set()

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < n

        while heap:
            current_t, i, j = heapq.heappop(heap)

            if (i, j) not in visited:
                visited.add((i, j))

                if (i, j) == (n-1, n-1):
                    return current_t
                
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j
                    if in_bounds(ii, jj) and (ii, jj) not in visited:
                        heapq.heappush(heap, 
                            (
                                max(current_t, grid[ii][jj]),
                                ii,
                                jj,
                            )
                        )