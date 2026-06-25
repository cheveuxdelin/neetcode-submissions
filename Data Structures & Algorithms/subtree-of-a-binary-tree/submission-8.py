# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def is_same_tree(self, t1, t2):
            if not t1:
                return not t2
            if not t2:
                return not t1
            return t1.val == t2.val and self.is_same_tree(t1.left, t2.left) and self.is_same_tree(t1.right, t2.right) 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return not subRoot
        if not subRoot:
            return True

        return self.is_same_tree(root, subRoot) or self.isSubtree(root.left, subRoot) or  self.isSubtree(root.right, subRoot)