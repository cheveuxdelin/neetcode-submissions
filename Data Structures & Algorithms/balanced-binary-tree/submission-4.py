# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # does checking for differing in depth give the same answer as differing in height?
        # i think that yes because counting is a symmetrical operation and a > b == b < a

        # returns (depth, is_balanced)
        def helper(current):
            if not current:
                return 0, True
            
            left_depth, left_is_balanced = helper(current.left)
            right_depth, right_is_balanced = helper(current.right)

            current_is_balanced = abs(left_depth - right_depth) <= 1
            current_depth = max(left_depth, right_depth) + 1

            return (current_depth, left_is_balanced and right_is_balanced and current_is_balanced)
        return helper(root)[1]
