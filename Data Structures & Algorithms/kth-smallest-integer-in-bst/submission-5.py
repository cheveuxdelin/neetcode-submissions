# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = 0

        def helper(current):
            nonlocal c
            if current:
                left = helper(current.left)
                if left != -1:
                    return left
                c += 1
                if c == k:
                    return current.val
                right = helper(current.right)
                if right != -1:
                    return right
            return -1

        return helper(root)