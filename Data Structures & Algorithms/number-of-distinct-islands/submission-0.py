class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        # we need to convert an island to a computed id
        # for every island found, add it to a set of unique ids
        # return the size of this set of unique ids
        # max size of the grid is 2500 cells
        # the bigger the island the bigger the key but the less available spaces
        # to make a unique id: get the island position, relative translations, and then sort
        # we dont need visited since we can be turning off the islands (setting 1 to 0)

        n = len(grid)
        m = len(grid[0])
        unique_islands = set()
        # visited = set()

        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0],
        ]

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m
        
        def helper(starting_row: int, starting_col: int, i: int, j: int, island: list[tuple[int, int]]):
            relative_i = i - starting_row
            relative_j = j - starting_col

            #visited.add((i, j))
            grid[i][j] = 0
            island.append((relative_i, relative_j))

            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and grid[ii][jj] == 1:
                    helper(starting_row, starting_col, ii, jj, island)

        for i in range(n):
            for j in range(m):
                # we found an island
                if grid[i][j] == 1:
                    island_array = []
                    helper(i, j, i, j, island_array)
                    island_array.sort()
                    island_array_as_tuple = tuple(island_array)
                    unique_islands.add(island_array_as_tuple)
        return len(unique_islands)
















