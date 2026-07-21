"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:

        # list[(best_diameter, number_of_nodes)]
        best_diameter = 0
        number_of_nodes = 1
        def helper(current):
            if not current:
                return (0, 0)

            children_results = [helper(child) for child in current.children]
            biggest_two_depths = heapq.nlargest(2, [result[number_of_nodes] for result in children_results])
            current_number_of_nodes = 1 + max([result[number_of_nodes] for result in children_results], default=0)

            return (
                max(
                    max([result[best_diameter] for result in children_results], default=0),
                    sum(biggest_two_depths),
                ),
                current_number_of_nodes,
            )
        return helper(root)[best_diameter]