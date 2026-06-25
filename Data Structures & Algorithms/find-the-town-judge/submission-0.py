class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(set)
        sset = set()

        for u, v in trust:
            graph[u].add(v)
            sset.add(u)
            sset.add(v)
        
        element_not_in_graph = None
        for c in sset:
            if c not in graph:
                if element_not_in_graph == None:
                    element_not_in_graph = c
                else:
                    return -1
        for k in graph:
            if element_not_in_graph not in graph[k]:
                return -1
        return element_not_in_graph
        
