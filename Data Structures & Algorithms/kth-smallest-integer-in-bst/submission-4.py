# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        
        def helper(current):
            nonlocal n
            if not current:
                return None
            if (result := helper(current.left)):
                return result
            n += 1
            if n == k:
                return current
            if (result := helper(current.right)):
                return result
            return None
        return helper(root).val