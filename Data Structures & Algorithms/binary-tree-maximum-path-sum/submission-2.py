# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -sys.maxsize

        def helper(current):
            nonlocal result

            if not current:
                return 0
            
            left = helper(current.left)
            right = helper(current.right)

            best = max(
                current.val,
                current.val + left,
                current.val + right,
                current.val + left + right
            )
            result = max(result, best)
            
            return max(
                current.val,
                current.val + left,
                current.val + right
            )
        helper(root)
        return result