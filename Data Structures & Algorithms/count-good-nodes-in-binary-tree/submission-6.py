# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0

        def helper(current, max_so_far):
            nonlocal result
            if current:
                if max_so_far <= current.val:
                    result += 1
                helper(current.left, max(max_so_far, current.val))
                helper(current.right, max(max_so_far, current.val))
        helper(root, -sys.maxsize)
        return result
