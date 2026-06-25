"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        d = {}

        def helper(current):
            if not current:
                return None
            d[current] = Node(current.val)
            for child in current.children:
                d[current].children.append(helper(child))
            return d[current]
        
        return helper(root)

        
        