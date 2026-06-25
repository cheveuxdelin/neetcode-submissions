
# if result, return topological sort
# return any valid ordering
# if not result (cycle)? return empty list
# n > 1? yes
# cycles? yes
# directed? yes
# vertex are 0-indexed
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        result = []
        
        graph = collections.defaultdict(list)
        visited = set()
        path = set()

        for u, v in edges:
            graph[u].append(v)

        # only unvisited nodes will go inside dfs
        def dfs(i):
            visited.add(i)
            path.add(i)
            for neighbor in graph[i]:
                if neighbor in path:
                    return True
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            path.discard(i)
            result.append(i)
            return False

        for i in range(n):
            if i not in visited:
                if dfs(i):
                    return []

        return list(reversed(result))