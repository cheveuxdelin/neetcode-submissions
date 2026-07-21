# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def helper(current, current_max):
            nonlocal result
            if current:
                if current_max <= current.val:
                    result += 1
                helper(current.left, max(current_max, current.val))
                helper(current.right, max(current_max, current.val))
        helper(root, root.val)
        return result