class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n
        def find(n):
            if parent[n] == n:
                return n
            parent[n] = find(parent[n])
            rank[n] = 1
            return parent[n]
        
        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p1] += 1
            
            return 1
        
        result = n
        for a, b in edges:
            result -= union(a, b)
        return result
