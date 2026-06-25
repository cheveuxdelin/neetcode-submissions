# unlimited amounts of each coin
# each coin unique
# no negative coins
from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def f(i, current):
            if current == amount:
                return 1
            elif current < amount and i < len(coins):
                return f(i+1, current) + f(i, current+coins[i])
            return 0
        return f(0, 0)
