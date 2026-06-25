# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = 0
        self.result = None
        def helper(current):
            if current:
                helper(current.left)
                self.k += 1
                if self.k == k:
                    self.result = current
                    return
                helper(current.right)

        helper(root)
        return self.result.val