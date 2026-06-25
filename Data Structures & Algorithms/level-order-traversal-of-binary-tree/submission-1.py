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

        queue = [root]

        while queue:
            result.append([node.val for node in queue])
            new_level = []
            for node in queue:
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            queue = new_level
        return result

