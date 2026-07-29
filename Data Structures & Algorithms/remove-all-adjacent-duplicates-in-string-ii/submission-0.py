class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        to_compare = list(s)
        next_iteration = True
        while next_iteration:
            next_iteration = False
            stack = []
            current_count = 0
            for c in to_compare:
                current_count = current_count + 1 if stack and stack[-1] == c else 1
                stack.append(c)
                if current_count == k:
                    next_iteration = True
                    for _ in range(k):
                        stack.pop()
            to_compare = stack
        return "".join(to_compare)
            


