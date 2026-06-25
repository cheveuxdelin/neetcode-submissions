class Solution:

    def manhattan_distance(self, point1: tuple[int, int], point2: tuple[int, int]) -> int:
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        heap = [(0, 0)]
        total_cost = 0
        while len(visited) < n:
            current_cost, current_node = heapq.heappop(heap)
            if current_node not in visited:
                visited.add(current_node)
                total_cost += current_cost
                for next_node in range(n):
                    if next_node not in visited:
                        heapq.heappush(heap, (self.manhattan_distance(points[current_node], points[next_node]), next_node))
        return total_cost