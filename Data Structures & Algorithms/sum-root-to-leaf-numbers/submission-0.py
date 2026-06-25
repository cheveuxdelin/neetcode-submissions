# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        result = 0

        def helper(current):
            nonlocal result
            path.append(current)

            if not current.left and not current.right:
                computed = 0
                i = 0
                for num in reversed(path):
                    computed += num.val * 10**i
                    i += 1
                result += computed
            else:
                if current.left:
                    helper(current.left)
                if current.right:
                    helper(current.right)
            path.pop()
        helper(root)
        return result
