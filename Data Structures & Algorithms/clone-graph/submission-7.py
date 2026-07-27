"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# insight here is that, if you are creating while you are enqueueing,
# that means that for the first iteration, the initial node should have already been duplicated
# be always mindful of not following your own defined order or operations
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        graph = {}
        queue = [node]
        graph[node] = Node(node.val)
        # do we need to track for visited?
        # there's no mention of lack of cycles so yes?
        visited = set([node])

        while queue:
            current = queue.pop()
            for neighbor in current.neighbors:
                if neighbor not in graph:
                    graph[neighbor] = Node(neighbor.val)
                graph[current].neighbors.append(graph[neighbor])
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return graph[node]
                

            