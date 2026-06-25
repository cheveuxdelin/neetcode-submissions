import functools

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp(remaining, i) = number of ways to form remaining using coins[i:]
        @functools.cache
        def dp(remaining, i):
            if remaining == 0:
                return 1
            elif remaining > 0 and i < len(coins):
                # skip current coin
                skip = dp(remaining, i+1)
                # take current coin
                take = dp(remaining-coins[i], i)
                return skip + take
            else:
                return 0
        return dp(amount, 0)
