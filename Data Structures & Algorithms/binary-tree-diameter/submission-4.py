# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # returns (depth, max_diameter)
        def helper(current):
            if not current:
                return (0, 0)

            left_depth, left_max_d = helper(current.left)
            right_depth, right_max_d = helper(current.right)

            left_edges = (left_depth + 1) if current.left else 0
            right_edges = (right_depth + 1) if current.right else 0
            current_n_edges = left_edges + right_edges
            current_depth = max(left_edges, right_edges)
            best_diameter = max(
                left_max_d,
                right_max_d,
                current_n_edges,
            )

            return (current_depth, best_diameter)
        return helper(root)[1]
