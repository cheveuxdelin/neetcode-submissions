# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(current, left_boundary, right_boundary):
            current_node_is_valid = left_boundary < current.val < right_boundary
            left_is_bst = True if not current.left else helper(current.left, left_boundary, current.val)
            right_is_bst = True if not current.right else helper(current.right, current.val, right_boundary)

            return current_node_is_valid and left_is_bst and right_is_bst
        return helper(root, -sys.maxsize, sys.maxsize)

