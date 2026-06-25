# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(node):
            if not node:
                return 0, True
            left_h, left_v = helper(node.left)
            right_h, right_v = helper(node.right)
            return 1 + max(left_h, right_h), abs(left_h - right_h) <= 1 and left_v and right_v
        return helper(root)[1]