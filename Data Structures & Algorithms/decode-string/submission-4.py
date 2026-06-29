class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                current = []
                while stack[-1] != "[":
                    current.append(stack.pop())
                current.reverse()

                stack.pop()
                
                numbers = []
                while stack and stack[-1].isnumeric():
                    numbers.append(stack.pop())
                numbers.reverse()

                stack.append("".join(current) * int("".join(numbers)))
            else:
                stack.append(c)
        return "".join(stack)