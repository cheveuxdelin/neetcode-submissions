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
        
        node_map = {}

        def dfs(current):
            new_node = Node(current.val)
            node_map[current] = new_node
            for neighbor in current.neighbors:
                if neighbor in node_map:
                    new_node.neighbors.append(node_map[neighbor])
                else:
                    new_node.neighbors.append(dfs(neighbor))
            return new_node
        

        return dfs(node)