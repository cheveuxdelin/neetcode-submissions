# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(current):
            if not current:
                return True, 0
            left_valid, left_height = helper(current.left)
            right_valid, right_height = helper(current.right)
            return left_valid and right_valid and abs(left_height - right_height) <= 1, max(left_height, right_height) + 1
        return helper(root)[0]