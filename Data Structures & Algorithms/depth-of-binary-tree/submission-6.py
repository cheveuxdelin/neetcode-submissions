# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(current):
            if not current:
                return 0
            
            left = helper(current.left)
            right = helper(current.right)

            return max(left, right) + 1
        return helper(root)