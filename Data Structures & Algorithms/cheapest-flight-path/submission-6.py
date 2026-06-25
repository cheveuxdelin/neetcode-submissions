class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, cost in flights:
            graph[u].append((v, cost))
        
        # (cost, k, i)
        heap = [(0, 0, src)]
        # (k, i)
        visited = set()

        while heap:
            current_cost, current_k, current = heapq.heappop(heap)

            if current == dst:
                return current_cost

            if (current_k, current) not in visited:
                visited.add((current_k, current))
                for neighbor, cost_to_neighbor in graph[current]:
                    if current_k < k+1 and (current_k+1, neighbor) not in visited:
                        heapq.heappush(heap, (current_cost+cost_to_neighbor, current_k+1, neighbor))
        return -1
