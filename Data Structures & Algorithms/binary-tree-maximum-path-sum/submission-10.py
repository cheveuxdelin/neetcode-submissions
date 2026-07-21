# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # (best_result, biggest_sum)
        def helper(current):
            if not current:
                return (-math.inf, 0)

            left_best_result, left_biggest_sum = helper(current.left)
            right_best_result, right_biggest_sum = helper(current.right)

            current_best_result = current.val + max(left_biggest_sum, 0) + max(right_biggest_sum, 0)
            current_biggest_sum = current.val + max(left_biggest_sum, right_biggest_sum, 0)

            return (
                max(
                    left_best_result,
                    right_best_result,
                    current_best_result
                ),
                current_biggest_sum
            )
        return helper(root)[0]