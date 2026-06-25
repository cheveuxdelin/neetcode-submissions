class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for origin, destination in tickets:
            graph[origin].append(destination)
        
        for origin in graph:
            graph[origin].sort(reverse=True)
        
        result = []

        def dfs(current):
            for neighbor in reversed(graph[current]):
                graph[current].pop()
                dfs(neighbor)
            result.append(current)
            

        dfs("JFK")
        return result[::-1]