class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # since it's a weighted graph, no bfs/dfs
        # dijkstra!
        # min_time for signal to reach all nodes = max_cost
        graph = [[] for _ in range(n+1)]

        for u, v, w in times:
            graph[u].append((v, w))

        distances = [-1] * (n+1)
        heap = [(0, k)]
        nodes_reached = 0

        while heap:
            current_distance, current = heapq.heappop(heap)
            if distances[current] == -1:
                distances[current] = current_distance
                nodes_reached += 1
                if nodes_reached == n:
                    return current_distance

                for neighbor, distance_to_neighbor in graph[current]:
                    if distances[neighbor] == -1:
                        heapq.heappush(heap, (current_distance+distance_to_neighbor, neighbor))
        # there can be no solution, so we return -1
        return -1