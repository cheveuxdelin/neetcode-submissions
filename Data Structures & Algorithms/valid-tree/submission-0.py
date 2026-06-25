class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [0 for _ in range(n)]
        self.n_sets = n
    
    def find(self, i: int) -> int:
        if i == self.parent[i]:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i: int, j: int):
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
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for u, v in edges:
            if not uf.union(u, v):
                return False
        
        return uf.n_sets == 1