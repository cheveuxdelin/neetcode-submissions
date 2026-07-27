# given the value of the MST
# a critical edge is present in all versions of a MST
# a pseudo edge, is in at least 1 version of the MST

# given these notions, we can obviously iterate over the edges
# and for each, avoiding it in the building of the mst
# if it builds the same MST, its at least a pseudo critical
# if its in all of the MSTs, is criitcal


class UnionFind:
    def __init__(self, n: int):
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

        if parent_i == parent_j:
            return False

        if self.size[parent_i] > self.size[parent_j]:
            self.parent[parent_j] = parent_i
            self.size[parent_i] += self.size[parent_j]
        else:
            self.parent[parent_i] = parent_j
            self.size[parent_j] += self.size[parent_i]

        self.n_groups -= 1
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        # we sort by weights, lowest weight first (kruskal)
        sorted_edges = sorted([*enumerate(edges)], key=lambda x: x[1][2])

        # lets calculate mst
        def calculate_mst(index_to_avoid: int, uf: UnionFind | None = None, value: int = 0) -> int:
            if not uf:
                uf = UnionFind(n)
            
            if uf.n_groups == 1:
                return value

            for i, (_, (u, v, w)) in enumerate(sorted_edges):
                if i != index_to_avoid:
                    if uf.union(u, v):
                        value += w
                    if uf.n_groups == 1:
                        return value
            return -1

        mst = calculate_mst(-1)
        critical = []
        pseudocritical = []

        for i, (original_index, (u, v, w)) in enumerate(sorted_edges):
            # critical: if by avoiding it, we can't reach the mst
            if calculate_mst(i) != mst:
                critical.append(original_index)
            # pseudo_critical: if by forcing it, we can reach one mst
            else:
                uf_forcing_edge = UnionFind(n)
                value = 0
                uf_forcing_edge.union(u, v)
                if calculate_mst(i, uf_forcing_edge, w) == mst:
                    pseudocritical.append(original_index)
        return [critical, pseudocritical]



