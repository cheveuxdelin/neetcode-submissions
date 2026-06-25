class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        result = 0
        visited = [False] * n

        def f(i):
            if visited[i]:
                return 0
            else:
                visited[i] = True
                for neighbor in adj[i]:
                    f(neighbor)
                return 1

        for i in range(n):
            result += f(i)
        return result
        