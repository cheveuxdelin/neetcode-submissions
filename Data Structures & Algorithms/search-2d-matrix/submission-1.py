class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def condition(i, j):
            return matrix[i][j] > target

        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left < right:
            mid = (left + right) // 2

            i, j = divmod(mid, len(matrix[0]))
            if matrix[i][j] == target:
                return True
            elif condition(i, j):
                right = mid
            else:
                left = mid + 1
        
        i, j = divmod(left, len(matrix[0]))
        return matrix[i][j] == target