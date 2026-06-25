# https://neetcode.io/problems/matchsticks-to-square/history?submissionIndex=8
import functools


class Solution:
    def makesquare(self, matchsticks: list[int]) -> bool:
        total_length = sum(matchsticks)
        if total_length % 4:
            return False
        target = total_length // 4

        matchsticks.sort(reverse=True)

        @functools.cache
        def helper(i: int, sides: tuple[int]) -> bool:
            if i == len(matchsticks):
                return all(side == target for side in sides)

            for side_index in range(4):
                if sides[side_index] + matchsticks[i] <= target:
                    new_sides = list(sides)
                    new_sides[side_index] += matchsticks[i]

                    if helper(i+1, tuple(sorted(new_sides))):
                        return True
            return False
        return helper(0, (0,0,0,0))
