class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1),
        ]
        
        def dfs(i, j, replacing):
            board[i][j] = replacing
            for di, dj in directions:
                ii = i+di
                jj = j+dj
                if 0 <= ii < n and 0 <= jj < m and board[ii][jj] == "O":
                    dfs(ii, jj, replacing)
        
        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0, "#")
            if board[i][m-1] == "O":
                dfs(i, m-1, "#")
        
        for j in range(m):
            if board[0][j] == "O":
                dfs(0, j, "#")
            if board[n-1][j] == "O":
                dfs(n-1, j, "#")
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
                
        