class UnionFind:
    def __init__(self, n: int):
        self.parent = [*range(n)]
        self.size = [1] * n
        self.n_groups = n
    
    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i: int, j: int) -> bool:
        parent_i = self.find(i)
        parent_j = self.find(j)

        # already together
        if parent_i ==  parent_j:
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # minimum cost to connect all points really means to find MST
        # multiple ways to do it, i know that using union find i'd be able to
        # find the next smallest edge and add it
        # i'd do this until all are connected

        n = len(points)
        uf = UnionFind(n)
        result = 0

        def calculate_distance(point1: list[int], point2: list[int]) -> int:
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        edges = [(calculate_distance(points[i], points[j]), i, j) for i in range(n-1) for j in range(i+1, n)]
        i = 0
        edges.sort()

        while uf.n_groups > 1:
            cost, a, b = edges[i]
            if uf.union(a, b):
                result += cost
            i += 1
        return result



