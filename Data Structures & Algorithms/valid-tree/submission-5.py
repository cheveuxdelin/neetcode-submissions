# this is essentially checking if there's a cycle in an undirected graph
# since a tree is undirected/connected/acyclical
# we just gotta check if this is true.

class UnionFind:
    def __init__(self, n: int) -> None:
        self.n_groups = n
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i: int, j: int) -> bool:
        parent_i = self.find(i)
        parent_j = self.find(j)

        # already connected, cycle
        if parent_i == parent_j:
            return False
        
        if self.size[parent_i] > self.size[parent_i]:
            self.parent[parent_j] = parent_i
            self.size[parent_i] += self.size[parent_j]
        else:
            self.parent[parent_i] = parent_j
            self.size[parent_j] += self.size[parent_i]
        
        self.n_groups -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # from the start we know there are extra edges
        if len(edges) != n - 1:
            return False
        uf = UnionFind(n)

        # now that we know there are exactly n-1 edges,
        # every one of them should be a correct merge
        # if not, its connecting something already connected.
        # cycle
        for u, v in edges:
            if not uf.union(u, v):
                return False
        return True
