class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # this is a postorder traversal
        # we gotta recollect all leaf nodes
        # and work back, getting the parent of the leaf nodes as the new leaf nodes
        # until we reach JFK

        result = []
        graph = collections.defaultdict(list)

        for u, v in tickets:
            graph[u].append(v)

        # should this sorting be reversed?
        for airport in graph:
            graph[airport].sort(reverse=True)

        # should we check for visited?
        # i don't think so since it's guaranteed for this to have a single valid path
        # but we do want to be discarding since every ticket can only be used once,
        # so it's a yes/no response
        def dfs(current: str):
            while graph[current]:
                dfs(graph[current].pop())
            result.append(current)
        
        dfs("JFK")
        result.reverse()
        return result
                