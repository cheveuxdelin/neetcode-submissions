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
            if board[i][j] != word[index]:
                return False
            if index == len(word)-1:
                return True

            board[i][j] = ""
            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj):
                    if helper(ii, jj, index+1):
                        return True
            board[i][j] = word[index]
            return False

        
        for i in range(n):
            for j in range(m):
                if helper(i, j, 0):
                    return True
        return False
                        