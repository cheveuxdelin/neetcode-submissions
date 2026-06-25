class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # (index, temperature)
        result = [0] * len(temperatures)

        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                index_in_stack = stack.pop()[0]
                number_of_days_for_warmer_temperature = index - index_in_stack
                result[index_in_stack] = number_of_days_for_warmer_temperature
            stack.append((index, temperature))
        return result