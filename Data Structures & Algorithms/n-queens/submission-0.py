class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        current = []
        grid = [[0] * n for _ in range(n)]

        def check_bounds(i, j):
            return 0 <= i < n and 0 <= j < n

        def add_or_remove_queen(i, j, aor):
            grid[i][j] += aor

            for row in range(n):
                if row != i:
                    grid[row][j] += aor
            for col in range(n):
                if col != j:
                    grid[i][col] += aor
            
            directions = [
                (1, 1),
                (-1, 1),
                (-1, -1),
                (1, -1)
            ]

            for di, dj in directions:
                ii, jj = i+di, j+dj
                while check_bounds(ii, jj):
                    grid[ii][jj] += aor
                    ii, jj = ii+di, jj+dj
        
        def build_current_solution():
            solution = [["."] * n for _ in range(n)]
            for i, j in current:
                solution[i][j] = "Q"
            return ["".join(row) for row in solution]

        def next_index(i, j):
            if i == j == n-1:
                return -1, -1
            elif j == n-1:
                return i+1, 0
            else:
                return i, j+1
        
        def dfs(i, j):
            if len(current) == n:
                result.append(build_current_solution())
            else:
                while i != -1:
                    if not grid[i][j]:
                        current.append((i, j))
                        add_or_remove_queen(i, j, 1)
                        dfs(*next_index(i, j))
                        current.pop()
                        add_or_remove_queen(i, j, -1)
                    i, j = next_index(i, j)
        dfs(0, 0)
        return result







