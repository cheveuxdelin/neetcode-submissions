class UnionFind:
    def __init__(self, n: int):
        self.n_groups = n
        self.parent = [*range(n)]
        self.size = [1] * n
    
    def find(self, i: int) -> int:
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i: int, j: int) -> bool:
        parent_i = self.find(i)
        parent_j = self.find(j)

        if parent_i == parent_j:
            return False
        
        if self.size[parent_i] < self.size[parent_j]:
            self.parent[parent_i] = parent_j
            self.size[parent_j] += self.size[parent_i]
        else:
            self.parent[parent_j] = parent_i
            self.size[parent_i] += self.size[parent_j]
        
        self.n_groups -= 1
        return True

class Solution:

    def manhattan_distance(self, point1: tuple[int, int], point2: tuple[int, int]) -> int:
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        uf = UnionFind(len(points))
        total_cost = 0

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                heapq.heappush(heap, (
                    self.manhattan_distance(points[i], points[j]),
                    i,
                    j
                ))
        
        while uf.n_groups > 1:
            current_cost, u, v = heapq.heappop(heap)
            if uf.union(u, v):
                total_cost += current_cost
        return total_cost
