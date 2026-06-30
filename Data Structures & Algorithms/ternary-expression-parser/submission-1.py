class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []

        for c in reversed(expression):
            if c == ":":
                continue
            
            if stack and stack[-1] == "?":
                stack.pop() # ?

                true_branch = stack.pop()
                false_branch = stack.pop()

                if c == "T":
                    stack.append(true_branch)
                else:
                    stack.append(false_branch)
            else:
                stack.append(c)
        return stack[0]