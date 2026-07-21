# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = collections.deque([root])
        none_found = False

        while queue:
            current = queue.popleft()

            for child in (current.left, current.right):
                if not child:
                    none_found = True
                else:
                    if none_found:
                        return False
                    queue.append(child)
        return True
            