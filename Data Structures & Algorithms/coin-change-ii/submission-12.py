import functools

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @functools.cache
        # dp(remaining, i) = number of ways that you can reach 0, starting from remaining and coin index
        def dp(remaining: int, i: int):
            if remaining == 0:
                return 1
            if i == len(coins):
                return 0
            
            # skip
            result = dp(remaining, i+1)

            # take
            if coins[i] <= remaining:
                result += dp(remaining-coins[i], i)

            return result
        return dp(amount, 0)