"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # we just have to find the root without parent
        # we can reconstruct the tree thru a parent[node] = node_that_is_parent
        # solution is to find the node that is not in the parent dictionary

        parent = {}

        # we gotta first find the leaf nodes
        leaf_nodes = [node for node in tree if not node.children]
        found = set(leaf_nodes)
        not_found = [node for node in tree if node.children]

        while not_found:
            next_not_found = []

            for node in not_found:
                all_children_found = True

                for child in node.children:
                    parent[child] = node

                    if child not in found:
                        all_children_found = False

                if all_children_found:
                    found.add(node)
                else:
                    next_not_found.append(node)
            not_found = next_not_found
        
        for node in tree:
            if node not in parent:
                return node


