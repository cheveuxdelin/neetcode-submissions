class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.lstrip("-").isnumeric():
                stack.append(int(token))
            elif token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                stack.append(int(second / first))
        return stack[0]