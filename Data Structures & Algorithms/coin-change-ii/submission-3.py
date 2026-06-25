import functools

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp(amount, i) = number of ways you can form amount using coins up to i
        @functools.cache
        def dp(current, i):
            if current == amount:
                return 1
            elif current < amount and i < len(coins):
                result = 0
                # skip current coin
                result += dp(current, i+1)
                # take current coin
                result += dp(current+coins[i], i)
                return result
            else:
                return 0
        return dp(0, 0)
