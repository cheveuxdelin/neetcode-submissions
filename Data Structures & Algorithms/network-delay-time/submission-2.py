
# nodes are 1 to n
# no negative weights
# if solution: return min time for all n nodes to receive the signal
# if no solution: return -1
# no cycles?

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # unvisited
        # unreachable
        distances = [sys.maxsize] * (n+1)
        heap = [(0, k)]

        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if distances[current_node] == sys.maxsize:
                distances[current_node] = current_distance

                for neighbor, distance_to_neighbor in graph[current_node]:
                    if distances[neighbor] == sys.maxsize:
                        heapq.heappush(heap, (current_distance+distance_to_neighbor, neighbor))

        return result if (result := max(distances[1:])) != sys.maxsize else -1