# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        stack = []

        def helper(current):
            nonlocal result
            if current:
                if not current.left and not current.right:
                    result += not stack or stack[-1].val <= current.val
                else:
                    if not stack or stack[-1].val <= current.val:
                        result += 1
                        stack.append(current)
                    helper(current.left)
                    helper(current.right)
                    if stack and stack[-1] == current:
                        stack.pop()
        helper(root)
        return result
