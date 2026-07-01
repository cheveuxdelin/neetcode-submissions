class UnionFind:
    def __init__(self, n: int):
        self.parent = [*range(n)]
        self.size = [1] * n
        self.n_groups = n

    def find(self, i: int):
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
            self.size[parent_i] = self.size[parent_j]
        
        self.n_groups -= 1
        return True
        

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)


        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    uf.union(i, j)
        return uf.n_groups

