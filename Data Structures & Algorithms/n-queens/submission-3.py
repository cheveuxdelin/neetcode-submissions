from collections.abc import Callable


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [[False] * n for _ in range(n)]
        cols = set()
        diag1 = set()
        diag2 = set()
        result = []

        def process_result():
            rows = []
            for row in grid:
                rows.append("".join(["Q" if cell else "." for cell in row]))
            result.append(rows)

        def backtrack(row: int):
            if row == n:
                process_result()
            else:
                for col in range(n):
                    if col not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                        cols.add(col)
                        diag1.add(row - col)
                        diag2.add(row + col)
                        grid[row][col] = True
                        backtrack(row+1)
                        cols.discard(col)
                        diag1.discard(row - col)
                        diag2.discard(row + col)
                        grid[row][col] = False
        backtrack(0)
        return result
