class UnionFind:
    def __init__(self, n: int):
        self.n_sets = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, i: int) -> int:
        if i == self.parent[i]:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i: int, j: int) -> bool:
        p_i = self.find(i)
        p_j = self.find(j)

        if p_i == p_j:
            return False
        
        if self.size[p_i] > self.size[p_j]:
            self.parent[p_j] = p_i
            self.size[p_i] += self.size[p_j]
        else:
            self.parent[p_i] = p_j
            self.size[p_j] += self.size[p_i]

        self.n_sets -= 1
        return True


class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        result = 0
        edges.sort(key=lambda edge: edge[2])
        uf = UnionFind(n)

        for u, v, w in edges:
            if uf.union(u, v):
                result += w
        return result if uf.n_sets == 1 else -1

