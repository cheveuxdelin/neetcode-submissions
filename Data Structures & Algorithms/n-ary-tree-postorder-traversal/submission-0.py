"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def helper(current):
            if current:
                for child in current.children:
                    helper(child)
                result.append(current.val)
        helper(root)
        return result