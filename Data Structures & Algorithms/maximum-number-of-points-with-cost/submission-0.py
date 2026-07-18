class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        m = len(points[0])

        # dp[i] = best score possible to reach row [i]
        dp = [[-sys.maxsize] * (m) for _ in range(n)]
        
        for j in range(m):
            dp[0][j] = points[0][j]
        
        for i in range(1, n):
            for j in range(m):
                best_score = -sys.maxsize
                for candidate_index in range(m):
                    best_score = max(
                        best_score,
                        dp[i-1][candidate_index] - abs(j - candidate_index) 
                    )
                dp[i][j] = points[i][j] + best_score
        return max(dp[-1])