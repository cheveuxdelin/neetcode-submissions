class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))
        
        # (current, ith_jump)
        visited = set()
        # (current_K, current_cost, current)
        heap = [(0, 0, src)]

        while heap:
            current_cost, ith_jump, current = heapq.heappop(heap)

            if current == dst:
                return current_cost
                
            if (current, ith_jump) not in visited:
                visited.add((current, ith_jump))
                for neighbor, cost_to_neighbor in graph[current]:
                    if ith_jump < k+1 and (neighbor, ith_jump+1) not in visited:
                        heapq.heappush(heap, (current_cost+cost_to_neighbor, ith_jump+1, neighbor))
        return -1
