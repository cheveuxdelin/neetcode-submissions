from collections.abc import Callable


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [[False] * n for _ in range(n)]
        attack_count = collections.defaultdict(int)
        result = []

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < n

        def populate(i: int, j: int, is_adding: bool):
            operation = 1 if is_adding else -1
            attack_count[(i, j)] += operation

            # horizontal
            for col in range(n):
                if col != j:
                    attack_count[(i, col)] += operation
            # vertical
            for row in range(n):
                if row != i:
                    attack_count[(row, j)] += operation

            # diagonals
            def process_diagonal(
                row: int, col: int, get_next_numbers: Callable[[int, int], tuple[int, int]]
            ):
                while in_bounds(row, col):
                    attack_count[(row, col)] += operation
                    row, col = get_next_numbers(row, col)

            process_diagonal(i - 1, j - 1, lambda row, col: (row - 1, col - 1))
            process_diagonal(i + 1, j + 1, lambda row, col: (row + 1, col + 1))
            process_diagonal(i + 1, j - 1, lambda row, col: (row + 1, col - 1))
            process_diagonal(i - 1, j + 1, lambda row, col: (row - 1, col + 1))

        def process_result():
            rows = []
            for row in grid:
                rows.append("".join(["Q" if cell else "." for cell in row]))
            result.append(rows)

        def backtrack(row: int):
            if row == n:
                process_result()
            else:
                for j in range(n):
                    if attack_count[(row, j)] == 0:
                        populate(row, j, True)
                        grid[row][j] = True
                        backtrack(row+1)
                        populate(row, j, False)
                        grid[row][j] = False

        backtrack(0)
        return result
