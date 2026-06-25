# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def helper(current, total):
            if not current.left and not current.right:
                return total == targetSum
            else:
                for child in (current.left, current.right):
                    if child and helper(child, total+child.val):
                        return True
                return False
        return helper(root, root.val) if root else False