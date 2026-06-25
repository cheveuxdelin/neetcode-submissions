class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]

        for u, v, cost in times:
            graph[u].append((cost, v))

        cost_to_reach_all_nodes = 0
        visited = set()
        heap = [(0, k)]

        while heap:
            current_cost, current_node = heapq.heappop(heap)
            if current_node not in visited:
                visited.add(current_node)
                cost_to_reach_all_nodes = max(cost_to_reach_all_nodes, current_cost)
                for cost_to_neighbor, neighbor in graph[current_node]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (current_cost+cost_to_neighbor, neighbor))
        return cost_to_reach_all_nodes if len(visited) == n else -1
