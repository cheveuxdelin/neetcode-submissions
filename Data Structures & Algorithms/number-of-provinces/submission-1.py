class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        result = 0

        def helper(i):
            visited[i] = True
            for j in range(n):
                if not visited[j] and isConnected[i][j]:
                    helper(j)

        for i in range(n):
            if not visited[i]:
                result += 1
                helper(i)
        
        return result