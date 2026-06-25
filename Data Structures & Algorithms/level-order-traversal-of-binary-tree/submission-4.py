# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        current_level = [root]

        while current_level:
            result.append([node.val for node in current_level])
            next_level = []
            for node in current_level:
                for child in node.left, node.right:
                    if child:
                        next_level.append(child)
            current_level = next_level
        return result

