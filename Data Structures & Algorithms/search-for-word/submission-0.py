class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        axis = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        visited = set()
        def backtrack(idx, i, j):
            if idx == len(word):
                return True
            elif (i, j) not in visited and 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[idx]:
                visited.add((i, j))
                for a_i, a_j in axis:
                    ii = a_i + i
                    jj = a_j + j
                    if backtrack(idx+1, ii, jj):
                        return True
                visited.discard((i, j))
                return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(0, i, j):
                    return True
        return False