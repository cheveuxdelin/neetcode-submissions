class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        left = 0
        right = n * m - 1

        while left < right:
            mid = (left + right) // 2
            div, mod = divmod(mid, m)

            if matrix[div][mod] >= target:
                right = mid
            else:
                left = mid + 1
        r, c = divmod(left, m)
        return matrix[r][c] == target