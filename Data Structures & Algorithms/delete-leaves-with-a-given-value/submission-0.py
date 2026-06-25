# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def f(current):
            if not current or (not current.left and not current.right and current.val == target):
                return True
            left = f(current.left)
            if left:
                current.left = None
            right = f(current.right)
            if right:
                current.right = None
            if left and right:
                return current.val == target

        dummy = TreeNode(0, root)
        f(dummy)
        return dummy.left