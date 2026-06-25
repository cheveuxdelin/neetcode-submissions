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
            return True
        
        if self.size[parent_i] < self.size[parent_j]:
            self.parent[parent_i] = parent_j
            self.size[parent_j] += parent_i
        else:
            self.parent[parent_j] = parent_i
            self.size[parent_i] += parent_j
        
        self.n_groups -= 1
        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        for a, b in edges:
            uf.union(a, b)
        return uf.n_groups
        