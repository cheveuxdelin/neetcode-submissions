# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(node):
            if not node:
                return 0, 0
            left_h, left_d = height(node.left)
            right_h, right_d = height(node.right)
            return 1 + max(left_h, right_h),  max(left_h + right_h, left_d, right_d)
        
        return height(root)[1]
        
            