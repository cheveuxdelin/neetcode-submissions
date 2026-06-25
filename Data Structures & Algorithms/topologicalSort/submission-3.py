
class Solution:
    def topologicalSort(self, n: int, edges: list[list[int]]) -> list[int]:
        result = []
        
        graph = collections.defaultdict(list)
        visited = set()
        path = set()
        
        for u, v in edges:
            graph[u].append(v)
        
        def dfs(i) -> bool:
            if i in visited:
                return False
            if i in path:
                return True
            
            path.add(i)
            
            for neighbor in graph[i]:
                if dfs(neighbor):
                    return True
            
            visited.add(i)
            path.discard(i)
            result.append(i)
        
        for i in range(n):
            if dfs(i):
                return []
        return list(reversed(result))