class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])

        directions = [
            (0, -1),
            (0, 1),
            (-1, 0),
            (1, 0),
        ]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m
        
        def helper(i, j, index):
            if index == len(word):
                return True
            else:
                for di, dj in directions:
                    ii = di+i
                    jj = dj+j
                    if in_bounds(ii, jj) and board[ii][jj] == word[index]:
                        tmp = word[index]
                        board[ii][jj] = ""
                        if helper(ii, jj, index+1):
                            return True
                        board[ii][jj] = tmp
                return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    board[i][j] = ""
                    if helper(i, j, 1):
                        return True
                    board[i][j] = word[0]

        return False
                        