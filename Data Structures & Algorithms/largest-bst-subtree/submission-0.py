import sys
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        # is_bst, size, min_val, max_val 
        def helper(current):
            nonlocal result

            if not current:
                return True, 0, sys.maxsize, -sys.maxsize
            
            l_is_bst, l_size, l_min, l_max = helper(current.left)
            r_is_bst, r_size, r_min, r_max = helper(current.right)

            if l_is_bst and r_is_bst and l_max < current.val < r_min:
                current_size = l_size + r_size + 1
                result = max(result, current_size)

                return (True, current_size, l_min if current.left else current.val, r_max if current.right else current.val)
            return False, 0, 0 ,0
        helper(root)
        return result