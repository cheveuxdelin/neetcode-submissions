class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)

        for u, v in edges:
            graph[u].append(v)

        if len(graph[destination]) > 0:
            return False

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        state = [0] * n

        def dfs(node) -> bool:
            if state[node] == VISITING:
                return False
            if state[node] == VISITED:
                return True
            
            if len(graph[node]) == 0:
                return node == destination
            
            state[node] = VISITING

            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            
            state[node] = VISITED
            return True
        
        return dfs(source)




