# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(last_max: int, current) -> int:
            rtn = 0
            if current:
                if current.val >= last_max:
                    rtn += 1
                    last_max = current.val
                rtn += helper(last_max, current.left) + helper(last_max, current.right)
            return rtn
        return helper(-math.inf, root)

        