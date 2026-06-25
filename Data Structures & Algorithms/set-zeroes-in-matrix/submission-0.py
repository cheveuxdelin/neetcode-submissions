class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # expand on a given location, avoids -1s
        def expand(i: int, j: int):
            for row in range(len(matrix)):
                if matrix[row][j] != -1:
                    matrix[row][j] = 0
            for col in range(len(matrix[0])):
                if matrix[i][col] != -1:
                    matrix[i][col] = 0
        
        # mark yet to process as -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = -1
        
        # process each -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
                    expand(i, j)
        
                    