class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, n: int) -> int:
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, a: int, b: int):
        p1 = self.find(a)
        p2 = self.find(b)

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += 1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)
        for a, b in edges:
            union_find.union(a, b)
        
        for i in range(n):
            union_find.find(i)
        return len(set(union_find.parent))