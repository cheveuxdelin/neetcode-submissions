class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        initial_color = image[sr][sc]
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
        
        if initial_color == color:
            return image

        def in_bounds(i: int, j: int) -> bool:
            return 0 <= i < n and 0 <= j < m

        def dfs(i: int, j: int):
            image[i][j] = color

            for di, dj in directions:
                ii = di+i
                jj = dj+j
                if in_bounds(ii, jj) and image[ii][jj] == initial_color:
                    dfs(ii, jj)
        
        dfs(sr, sc)
        return image