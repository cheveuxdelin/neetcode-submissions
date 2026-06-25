class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n+1)]

        for u, v, w in times:
            graph[u].append((v, w))

        distances = [sys.maxsize for _ in range(n+1)]
        heap = [(0, k)]

        while heap:
            distance, current = heapq.heappop(heap)
            if distances[current] == sys.maxsize:
                distances[current] = distance
                for neighbor, distance_to_neighbor in graph[current]:
                    if distances[neighbor] == sys.maxsize:
                        heapq.heappush(heap, (distance+distance_to_neighbor, neighbor))
        
        result = max(distances[i] for i in range(1, n+1))
        return result if result != sys.maxsize else -1