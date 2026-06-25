# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        def helper(current, current_sum):
            nonlocal result
            new_current_sum = current_sum * 10 + current.val

            if not current.left and not current.right:
                result += new_current_sum
            else:
                if current.left:
                    helper(current.left, new_current_sum)
                if current.right:
                    helper(current.right, new_current_sum)
        helper(root, 0)
        return result
