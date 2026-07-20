class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m
        
        def dfs(i: int, j: int, current_set: set):
            current_set.add((i, j))

            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and grid[ii][jj] == 1 and (ii, jj) not in current_set:
                    dfs(ii, jj, current_set)

        # from one island of the two, we gotta bfs
        # expand until we see the shortest path

        # step 1 is to locate and find the two islands
        island1 = set()
        island2 = set()

        for i in range(n):
            found = False
            for j in range(m):
                if grid[i][j] == 1:
                    dfs(i, j, island1)
                    found = True
                    break
            if found:
                break
        
        for i in range(n):
            found = False
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in island1:
                    dfs(i, j, island2)
                    found = True
                    break
            if found:
                break
        
        # now that we have the two islands traced, we will trace all the boundaries of one of the two

        queue = collections.deque(list(island1))
        visited = set(island1)
        current_jumps = 0

        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j

                    if (ii, jj) in island2:
                        return current_jumps

                    if in_bounds(ii, jj) and (ii, jj) not in visited:
                        visited.add((ii, jj))
                        queue.append((ii, jj))
            current_jumps += 1