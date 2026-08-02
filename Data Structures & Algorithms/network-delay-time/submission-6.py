class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u-1].append((v-1, w))

        distances = [sys.maxsize] * n
        # current_cost, current_node
        heap = [(0, k-1)]

        while heap:
            current_cost, current = heapq.heappop(heap)
            if distances[current] == sys.maxsize:
                distances[current] = current_cost

                for neighbor, cost_to_neighbor in graph[current]:
                    if distances[neighbor] == sys.maxsize:
                        heapq.heappush(heap, (current_cost + cost_to_neighbor, neighbor))

        result = max(distances)
        print(distances)
        return result if result != sys.maxsize else -1
