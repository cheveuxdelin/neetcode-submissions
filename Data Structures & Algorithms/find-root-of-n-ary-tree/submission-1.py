"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        children = set()

        for node in tree:
            for child in node.children:
                children.add(child)
        
        for node in tree:
            if node not in children:
                return node