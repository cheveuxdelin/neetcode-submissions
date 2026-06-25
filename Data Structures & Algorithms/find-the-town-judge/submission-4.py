class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(set)

        for u, v in trust:
            graph[u].add(v)
        
        judge = None
        for i in range(1, n+1):
            if i not in graph:
                if not judge:
                    judge = i
                else:
                    return -1
        if not judge:
            return -1
        for k in graph:
            if judge not in graph[k]:
                return -1
        return judge
