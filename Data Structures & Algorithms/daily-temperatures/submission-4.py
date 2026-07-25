class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        index = 0
        temperature = 1

        n = len(temperatures)
        result = [0] * n
        # (index, temperature)
        stack = []
        # this is just finding the next greater element
        # and find the distance between them
        # nothing crazy

        
        for i, num in enumerate(temperatures):
            # the elements in the stack are pending evaluation
            # we exhaust the stack for the ones we have found a solution 
            while stack and num > stack[-1][temperature]:
                popped_index = stack.pop()[index]
                result[popped_index] = i - popped_index
            stack.append((i, num))
        return result