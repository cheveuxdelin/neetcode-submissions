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
            if current.left:
                node, result = helper(current.left)
                if result:
                    return node, True
            n += 1
            if n == k:
                return current, True
            if current.right:
                node, result = helper(current.right)
                if result:
                    return node, True
            return current, False

        return helper(root)[0].val