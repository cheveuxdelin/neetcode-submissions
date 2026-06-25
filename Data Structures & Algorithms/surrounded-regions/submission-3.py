class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        directions = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0)
        ]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            board[i][j] = ""
            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and board[ii][jj] == "O":
                    dfs(ii, jj)
        
        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][m-1] == "O":
                dfs(i, m-1)
        for j in range(m):
            if board[0][j] == "O":
                dfs(0, j)
            if board[n-1][j] == "O":
                dfs(n-1, j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
