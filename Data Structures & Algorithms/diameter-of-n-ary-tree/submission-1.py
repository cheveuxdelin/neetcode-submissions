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
        
        def helper(current):
            if not current:
                return (0, 0)

            children_results = [helper(child) for child in current.children]
            c_best_diameters = [result[0] for result in children_results]
            c_depths = [result[1] for result in children_results]

            biggest_two_depths = heapq.nlargest(2, c_depths)
            current_number_of_nodes = 1 + max(c_depths, default=0)

            return (
                max(
                    max(c_best_diameters, default=0),
                    sum(biggest_two_depths),
                ),
                current_number_of_nodes,
            )
        return helper(root)[0]