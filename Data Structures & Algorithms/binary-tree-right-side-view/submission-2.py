# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = [root]
        result = [] # values of nodes

        while q:
            result.append(q[-1].val)
            next_iteration = []
            for current in q:
                if current.left:
                    next_iteration.append(current.left)
                if current.right:
                    next_iteration.append(current.right)
            q = next_iteration
        return result