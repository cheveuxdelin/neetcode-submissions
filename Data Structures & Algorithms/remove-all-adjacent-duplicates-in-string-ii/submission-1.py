class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        value = 0
        count = 1
        stack = []

        for c in s:
            if stack and stack[-1][value] == c:
                stack[-1][count] += 1
                if stack[-1][count] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        
        result = []

        for v, c in stack:
            result.extend(v * c)
        return "".join(result)


