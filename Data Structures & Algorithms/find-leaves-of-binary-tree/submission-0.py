# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def helper(current):
            if not current:
                return -1
            
            left_height = helper(current.left)
            right_height = helper(current.right)
            current_height = max(left_height, right_height) + 1

            if len(result) == current_height:
                result.append([])
            
            result[current_height].append(current.val)
            return current_height
        
        helper(root)
        return result