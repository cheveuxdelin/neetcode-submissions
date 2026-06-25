# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result = []

        def dfs(current):
            if not current:
                result.append("N")
                return 
            result.append(str(current.val))
            dfs(current.left)
            dfs(current.right)

        dfs(root)
        return ",".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        
        current = 0

        def dfs():
            nonlocal current
            if values[current] == "N":
                current += 1
                return None
            node = TreeNode(int(values[current]))
            current += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
