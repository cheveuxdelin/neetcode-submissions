class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for origin, destination in tickets:
            graph[origin].append(destination)
        
        for origin in graph:
            graph[origin].sort(reverse=True)

        visited = set()
        result = []

        def dfs(current: str):
            while graph[current]:
                dfs(graph[current].pop())
            result.append(current)
        
        dfs("JFK")
        return list(reversed(result))
