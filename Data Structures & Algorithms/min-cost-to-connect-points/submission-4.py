class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.n_sets = n
    
    def find(self, i: int) -> int:
        if i == self.parent[i]:
            return i
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
        
        self.n_sets -= 1
        return True

class Solution:
    def generate_all_distances(self, points: list[list[int]]) -> list[tuple[int, int, int]]:
        result = []

        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                a = points[i]
                b = points[j]
                result.append((abs(a[0]-b[0]) + abs(a[1]-b[1]), i, j))
        return result

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UnionFind(len(points))
        all_distances = self.generate_all_distances(points)
        heapq.heapify(all_distances)
        result = 0

        while uf.n_sets > 1:
            w, a, b = heapq.heappop(all_distances)
            if uf.union(a, b):
                result += w
        return result












        