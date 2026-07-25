class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        # (index, temperature)
        stack = []
        # we are looking for the next greater element
        # result is the amount of days to wait before it
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                popped = stack.pop()
                result[popped[0]] = i - popped[0]
            stack.append((i, temperature))
        return result