# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def f(current):
            # when checking child
            # if current is None or current is leaf with value target, it's safe to be set as None
            if not current or (not current.left and not current.right and current.val == target):
                return True

            left = f(current.left)
            right = f(current.right)
            
            if left:
                current.left = None
            if right:
                current.right = None
            if left and right:
                return current.val == target

        result = f(root)
        return root if not result else None