class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degrees = [0] * n
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degrees[u] += 1
            degrees[v] += 1
        
        leaf_nodes = [i for i in range(n) if len(graph[i]) == 1]
        queue = collections.deque(leaf_nodes)
        remaining_nodes = set(range(n))

        while len(remaining_nodes) > 2:
            for _ in range(len(queue)):
                current = queue.popleft()
                remaining_nodes.discard(current)
                
                for neighbor in graph[current]:
                    degrees[neighbor] -= 1
                    # it is now a leaf
                    if degrees[neighbor] == 1:
                        queue.append(neighbor)
        return list(remaining_nodes)

