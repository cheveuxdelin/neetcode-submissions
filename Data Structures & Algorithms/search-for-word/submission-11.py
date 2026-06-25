class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        def backtrack(i, j, current_index):
            if current_index == len(word):
                return True
            if not in_bounds(i, j) or visited[i][j] or board[i][j] != word[current_index]:
                return False
            visited[i][j] = True
            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if backtrack(ii, jj, current_index+1):
                    return True
            visited[i][j] = False

        
        for i in range(n):
            for j in range(m):
                if backtrack(i, j, 0):
                    return True
        return False