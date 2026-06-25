class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
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
    def generate_all_edges(self, points: List[List[int]]) -> list[list[int]]:
        result = []

        for i in range(len(points)-1):
                for j in range(i+1, len(points)):
                    distance = abs(points[i][0]-points[j][0]) + abs(points[i][1] - points[j][1])
                    result.append((i, j, distance))
        return result

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UnionFind(len(points))
        edges = self.generate_all_edges(points)
        edges.sort(key=lambda x:x[2])
        result = 0

        for u, v, w in edges:
            if uf.union(u, v):
                result += w
                if uf.n_sets == 1:
                    return result
        return result



        
            