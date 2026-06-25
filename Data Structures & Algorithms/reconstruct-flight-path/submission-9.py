class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for origin, destination in tickets:
            graph[origin].append(destination)
        
        for k in graph:
            graph[k].sort(reverse=True)
        
        result = []
        
        def dfs(current):
            while graph[current]:
                dfs(graph[current].pop())
            result.append(current)
        

        dfs("JFK")
        return list(reversed(result))