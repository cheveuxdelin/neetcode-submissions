# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        path_max = root.val

        def helper(node):
            nonlocal result, path_max

            if node.val >= path_max:
                result += 1
            
            for child in (node.left, node.right):
                if child:
                    old_path_max = path_max
                    path_max = max(path_max, node.val)
                    helper(child)
                    path_max = old_path_max
        
        helper(root)
        return result