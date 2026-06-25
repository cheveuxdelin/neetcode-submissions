# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = [[]]

        def helper(current):
            if not current.left and not current.right:
                result[0].append(current.val)
                return 0
            else:
                left_height = -1 if not current.left else helper(current.left)
                right_height = -1 if not current.right else helper(current.right)
                current_height = max(left_height, right_height) + 1

                if len(result) == current_height:
                    result.append([])
                
                result[current_height].append(current.val)
                return current_height
        
        helper(root)
        return result