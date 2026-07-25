class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # is the input valid?
        # will it always have two numbers before an operation?
        # what does it actually meanm integers always truncates toward zero
        # should we return something else if we are left with two numbers or theres an invalid order
        stack = []

        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif token == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif token == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif token == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(math.trunc(b / a))
            else:
                stack.append(int(token))
        return stack[0]