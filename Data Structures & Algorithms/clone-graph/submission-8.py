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

        graph = {node: Node(node.val)}
        queue = [node]

        while queue:
            current = queue.pop()
            for neighbor in current.neighbors:
                if neighbor not in graph:
                    graph[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                graph[current].neighbors.append(graph[neighbor])
        return graph[node]
                

            