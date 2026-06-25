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
            new_node = Node(current.val)
            d[current] = new_node

            for neighbor in current.neighbors:
                if neighbor not in d:
                    dfs(neighbor)
                new_node.neighbors.append(d[neighbor])
            
        
        dfs(node)
        return d[node]