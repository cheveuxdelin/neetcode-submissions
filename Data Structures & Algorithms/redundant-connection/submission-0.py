class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        d = defaultdict(list)


        def dfs(current, parent, visited):
            visited[current] = True
            for neighbor in d[current]:
                if neighbor != parent:
                    if visited[neighbor] or dfs(neighbor, current, visited):
                        return True
            return False

        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
            visited = [False] * (n+1)
            if dfs(u, -1, visited):
                return [u, v]
        return []