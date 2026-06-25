
# tickets[i] = [from, to]
# starting from JFK
# if result: return lexicographically smallest one
# if no result? there's at least 1 result
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        result = []

        for origin, destination in tickets:
            graph[origin].append(destination)

        for origin in graph:
            graph[origin].sort(reverse=True)
        
        def dfs(current):
            while graph[current]:
                dfs(graph[current].pop())
            result.append(current)
        
        dfs("JFK")
        return list(reversed(result))