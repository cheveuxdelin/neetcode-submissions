# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        answer = -sys.maxsize

        def helper(current):
            nonlocal answer
            if not current:
                return 0
            
            left = helper(current.left)
            right = helper(current.right)

            longest = 1

            if current.left and current.left.val == current.val + 1:
                longest = max(longest, left + 1)
            if current.right and current.right.val == current.val + 1:
                longest = max(longest, right + 1)
            
            answer = max(answer, longest)
            return longest
        helper(root)
        return answer
            
