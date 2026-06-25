# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(current):
            if current:
                if not current.left and not current.right:
                    return current.val == target
                
                d_left = helper(current.left)
                d_right = helper(current.right)

                if d_left:
                    current.left = None
                if d_right:
                    current.right = None

                if d_left and d_right:
                    return current.val == target
                else:
                    return False
            else:
                return True
        
        result = helper(root)

        if result:
            return None
        else:
            return root
        