# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(last_max: int, current) -> int:
            if not current:
                return 0
            
            new_max = max(last_max, current.val)
            return bool(current.val == new_max) + helper(new_max, current.left) + helper(new_max, current.right)
            
        return helper(-math.inf, root)

        