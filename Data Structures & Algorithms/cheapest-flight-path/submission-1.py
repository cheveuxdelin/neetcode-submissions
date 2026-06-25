class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))
        
        heap = [(0, 0, src)]
        visited = set()

        while heap:
            distance, n_jump, current = heapq.heappop(heap)
            if current == dst:
                return distance
            if (current, n_jump) not in visited:
                visited.add((current, n_jump))
                for neighbor, cost_to_neighbor in graph[current]:
                    new_cost = distance+cost_to_neighbor
                    if (neighbor, n_jump+1) not in visited and n_jump <= k:
                        heapq.heappush(heap, (new_cost, n_jump+1, neighbor))
        return -1