# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, left_boundary, right_boundary):
            if not node:
                return True
            
            left_is_bst = helper(node.left, left_boundary, node.val)
            right_is_bst = helper(node.right, node.val, right_boundary)

            return left_is_bst and right_is_bst and left_boundary < node.val < right_boundary

        return helper(root, -sys.maxsize, sys.maxsize)
