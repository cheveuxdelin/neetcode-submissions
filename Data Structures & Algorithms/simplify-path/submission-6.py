class Solution:
    def simplifyPath(self, path: str) -> str:
        # The path must start with a single slash '/'
        stack = []

        for split_path in path.split("/"):
            if split_path:
                if split_path == "..":
                    if stack:
                        stack.pop()
                elif split_path != ".":
                    stack.append(split_path)

        return "/" + "/".join(stack)