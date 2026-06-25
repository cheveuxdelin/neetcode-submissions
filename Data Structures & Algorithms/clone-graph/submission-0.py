"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        d = {}

        def dfs(current):
            if current in d:
                return d[current]

            new_node = Node(current.val)
            d[current] = new_node

            for neighbor in current.neighbors:
                new_node.neighbors.append(dfs(neighbor))
            return new_node
        
        return dfs(node) if node else None