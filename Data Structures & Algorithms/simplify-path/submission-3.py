class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for c in path.split("/"):
            if not c or c == ".":
                continue
            elif c != "..":
                stack.append(c)
            else:
                if stack:
                    stack.pop()
        return "/" + "/".join(stack)