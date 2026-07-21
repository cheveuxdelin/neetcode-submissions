# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        result = 0

        def helper(current, count):
            nonlocal result
            result = max(result, count)
            for child in (current.left, current.right):
                if child:
                    if child.val == current.val + 1:
                        helper(child, count+1)
                    else:
                        helper(child, 1)
        helper(root, 1)
        return result
