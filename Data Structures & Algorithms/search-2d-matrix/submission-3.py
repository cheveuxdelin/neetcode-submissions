class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        number_of_elements = n*m

        def get_index(input_n: int):
            div, mod = divmod(input_n, m)
            return (div, mod)
        
        left = 0
        right = number_of_elements - 1

        while left < right:
            mid = (left + right) // 2
            i, j = get_index(mid)
            if matrix[i][j] >= target:
                right = mid
            else:
                left = mid + 1
        i, j= get_index(left)
        return matrix[i][j] == target
        