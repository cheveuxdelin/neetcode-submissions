
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return result