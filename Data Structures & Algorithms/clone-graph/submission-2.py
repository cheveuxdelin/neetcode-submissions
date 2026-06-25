"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        d = {}

        def dfs(current):
            copy = Node(current.val)
            d[current] = copy

            for neighbor in current.neighbors:
                if neighbor not in d:
                    d[neighbor] = dfs(neighbor)
                copy.neighbors.append(d[neighbor])
            return copy
        return dfs(node)