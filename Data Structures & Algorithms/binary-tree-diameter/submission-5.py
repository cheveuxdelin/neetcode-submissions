# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def helper(current):
            if not current:
                return (0, 0)
            
            left_depth, left_max_d = helper(current.left)
            right_depth, right_max_d = helper(current.right)

            current_depth = max(left_depth, right_depth) + 1
            return (
                current_depth,
                max(left_max_d, right_max_d, left_depth + right_depth)
            )
        return helper(root)[1]


