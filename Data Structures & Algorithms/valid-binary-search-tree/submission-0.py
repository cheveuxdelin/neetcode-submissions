# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def convert_to_inorder_traversal(root) -> list:
            result = []

            def helper(current):
                if current:
                    helper(current.left)
                    result.append(current)
                    helper(current.right)
            helper(root)
            return result
        
        converted_to_array = convert_to_inorder_traversal(root)
        for i in range(1, len(converted_to_array)):
            if converted_to_array[i].val <= converted_to_array[i-1].val:
                return False
        return True