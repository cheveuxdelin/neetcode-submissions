class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = []
                while stack[-1] != "[":
                    substr.append(stack.pop())
                substr.reverse()
                stack.pop()

                k = []
                while stack and stack[-1].isdigit():
                    k.append(stack.pop())
                k = int("".join(reversed(k)))

                stack.append("".join(substr) * k)
        return "".join(stack)