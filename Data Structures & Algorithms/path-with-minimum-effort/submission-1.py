class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])

        directions = [
            (0, 1),
            (0,-1),
            (1, 0),
            (-1,0),
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m
        
        # cost, i, j
        heap = [(0, 0, 0)]
        visited = set()

        while heap:
            current_cost, i, j = heapq.heappop(heap)
            if (i, j) == (n-1, m-1):
                return current_cost
            if (i, j) not in visited:
                visited.add((i, j))
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j
                    if in_bounds(ii, jj) and (ii, jj) not in visited:
                        calculated_cost = abs(heights[ii][jj]-heights[i][j])
                        heapq.heappush(heap, (max(current_cost, calculated_cost), ii, jj))

            
