
# n nodes
# 0 indexed
# len(edges) == len(succProb) == n
# if solution: path with max probability
# if no solution: return 0
# start_node and end_node within n
# undirected (an edge goes both ways)
# needs a max heap
# need to be multiplying the probabilities
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = collections.defaultdict(list)

        for (u, v), probability in zip(edges, succProb):
            graph[v].append((u, probability))
            graph[u].append((v, probability))

        visited = set()
        heap = [(-1, start_node)]

        while heap:
            current_probability, current_i = heapq.heappop(heap)

            if current_i == end_node:
                return -current_probability
            elif current_i not in visited:
                visited.add(current_i)
                for neighbor, probability_to_neighbor in graph[current_i]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (
                            current_probability*probability_to_neighbor, #this will always do (+)*(-) = (-)
                            neighbor
                        ))
        return 0