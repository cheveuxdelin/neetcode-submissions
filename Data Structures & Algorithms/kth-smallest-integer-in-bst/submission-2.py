# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth = 0

        def helper(current):
            nonlocal kth
            if current.left and (result := helper(current.left)):
                return result
            kth += 1
            if kth == k:
                return current
            if current.right and (result := helper(current.right)):
                return result
            

        return helper(root).val