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
        current = [root]

        while current:
            result.append([element.val for element in current])
            next_iteration = []
            for node in current:
                if node.left:
                    next_iteration.append(node.left)
                if node.right:
                    next_iteration.append(node.right)
            current = next_iteration
        return result
