"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# sya the problem in my own words
# discuss input constraints and assumptions
# clarify edge/corner cases
# high level approach explanation and why is best
# dry run of my test cases
# does this make sense?
# code and narrate
# dry run again
# space & time complexity
# succeed

# can a neighbor be None?
# can the root be None?
# we assume correct input



# cycles?
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        d = {}

        def dfs(current):
            if current in d:
                return d[current]
            
            copied_node = Node(current.val)
            d[current] = copied_node

            for neighbor in current.neighbors:
                copied_node.neighbors.append(dfs(neighbor))
            return copied_node

        return dfs(node)