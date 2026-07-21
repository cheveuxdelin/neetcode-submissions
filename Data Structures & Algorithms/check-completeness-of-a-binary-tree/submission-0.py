# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        current_level = [root]
        none_found = False

        while current_level:
            next_level = []

            for node in current_level:
                for child in (node.left, node.right):
                    if not child:
                        none_found = True
                    else:
                        if none_found:
                            return False
                        next_level.append(child)
            current_level = next_level
        return True
            