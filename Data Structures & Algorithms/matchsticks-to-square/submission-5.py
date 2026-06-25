import functools

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4:
            return False
        target = total_length // 4

        current = [0,0,0,0]

        @functools.cache
        def helper(i: int, sides: tuple[int]) -> bool:
            if i == len(matchsticks):
                return all(side == target for side in sides)

            for side_index in range(4):
                if current[side_index] + matchsticks[i] <= target:
                    current[side_index] += matchsticks[i]

                    if helper(i+1, tuple(current)):
                        return True
                    current[side_index] -= matchsticks[i]
            return False
        return helper(0, tuple(current))