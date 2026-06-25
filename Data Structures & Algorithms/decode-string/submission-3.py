class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                # we now need to get the k
                # and the substring

                substr = []
                while stack[-1].isalpha():
                    substr.append(stack.pop())
                stack.pop() # removing the [
                substr = "".join(reversed(substr)) # return to order of appending

                k = []

                while stack and stack[-1].isdigit():
                    k.append(stack.pop())
                k = int("".join(reversed(k)))
                # need to:
                # reverse
                # join
                # convert to int

                stack.append(substr * k)
        return "".join(stack)