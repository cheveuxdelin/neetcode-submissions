# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        d1 = set()
        d2 = set()

        def helper(current, d):
            if current:
                d.add(current.val)
                
                helper(current.left, d)
                helper(current.right, d)
        
        helper(root1, d1)
        helper(root2, d2)

        for value in d1:
            other = target - value
            if other in d2:
                return True
        return False
