# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def helper(current):
            if not current:
                return (0, 0)
            
            # post order
            left_max, left_len = helper(current.left)
            right_max, right_len = helper(current.right)

            current_len = 1

            if current.left and current.left.val == current.val + 1:
                current_len = max(current_len, 1 + left_len)
            if current.right and current.right.val == current.val + 1:
                current_len = max(current_len, 1 + right_len)
            
            return (
                max(
                    left_max,
                    right_max,
                    current_len,
                ),
                current_len
            )
        return helper(root)[0]
