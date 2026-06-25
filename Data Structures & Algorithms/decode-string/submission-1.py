class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                substr = []
                while stack[-1] != "[":
                    substr.append(stack.pop())
                stack.pop()
                substr = "".join(reversed(substr))

                k = []
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())
                k = int("".join(reversed(k)))

                stack.append(k * substr)
            else:
                stack.append(c)
        return "".join(stack)