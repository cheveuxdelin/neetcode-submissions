class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        n = len(board)
        m = len(board[0])

        while True:
            to_delete = [[False] * m for _ in range(n)]
            is_deleting = False

            for i in range(n):
                for j in range(m):
                    val = board[i][j]
                    if val:
                        # horizontal
                        if j >= 2 and val == board[i][j-1] == board[i][j-2]:
                            to_delete[i][j] = to_delete[i][j-1] = to_delete[i][j-2] = True
                            is_deleting = True
                        # vertical
                        if i >= 2 and val == board[i-1][j] == board[i-2][j]:
                            to_delete[i][j] = to_delete[i-1][j] = to_delete[i-2][j] = True
                            is_deleting = True

            if not is_deleting:
                break
            
            # bubble down alive cells
            for j in range(m):
                write_row = n-1
                for i in reversed(range(n)):
                    if not to_delete[i][j]:
                        board[write_row][j] = board[i][j]
                        write_row -= 1
                while write_row >= 0:
                    board[write_row][j] = 0
                    write_row -= 1
        return board