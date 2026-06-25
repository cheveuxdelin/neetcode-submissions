# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, position = queue.popleft()
            if node:
                cols[position].append(node.val)
                queue.append((node.left, position - 1))
                queue.append((node.right, position + 1))
        
        return [cols[k] for k in sorted(cols)]