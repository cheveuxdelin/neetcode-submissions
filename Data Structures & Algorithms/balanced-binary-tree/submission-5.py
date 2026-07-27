# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# we need to check, for a given node
# if both left subtree is balanced, if right subtree is balanced
# and return our current height
# so our parent can calculate now if just computed subtree is also balanced
# bubbling the solution up so no work done twice

# problem asks for height, but depth is just height counted backwards, so symmetrical problem, symmetrical solution
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # returns (is_balanced, height)
        def helper(current):
            # an empty tree is completely balanced
            if not current:
                return True, 0
            
            left_is_balanced, left_depth = helper(current.left)
            right_is_balanced, right_depth = helper(current.right)

            current_is_balanced = left_is_balanced and right_is_balanced and abs(left_depth - right_depth) <= 1
            current_depth = 1 + max(left_depth, right_depth)

            return (
                current_is_balanced,
                current_depth
            )
        return helper(root)[0]