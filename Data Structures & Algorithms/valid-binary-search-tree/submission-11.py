# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(current, lowest_value, greatest_value):
            if not current:
                return True
            
            if not lowest_value < current.val < greatest_value:
                return False
            
            left_is_bst = helper(current.left, lowest_value, current.val)
            right_is_bst = helper(current.right, current.val, greatest_value)

            return left_is_bst and right_is_bst
        return helper(root, -sys.maxsize, sys.maxsize)
