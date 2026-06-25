# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(current):
            nonlocal result
            if current:
                dfs(current.left)
                result.append(current.val)
                dfs(current.right)
        dfs(root)
        return result
        