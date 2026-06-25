# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        def f(current):
            is_leaf_with_val = current and (not current.left and not current.right and current.val == target)
            if not current or is_leaf_with_val:
                return True

            left = f(current.left)
            right = f(current.right)
            
            if left:
                current.left = None
            if right:
                current.right = None
            return left and right and current.val == target
            

        result = f(root)
        return root if not result else None