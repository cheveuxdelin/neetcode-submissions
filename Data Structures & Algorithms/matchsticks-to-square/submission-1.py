from functools import cache
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        div, mod = divmod(sum(matchsticks), 4)

        if mod:
            return False
        
        target = div
        current = [0, 0, 0, 0]

        @cache
        def f(i, current_tuple):
            if i == len(matchsticks):
                return current[0] == current[1] == current[2] == current[3]
            elif i < len(matchsticks):
                for side in range(4):
                    current[side] += matchsticks[i]
                    if f(i+1, tuple(current)):
                        return True
                    current[side] -= matchsticks[i]
            return False
        return f(0, tuple(current))