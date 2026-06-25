import sys
import functools

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp(x) = number of ways for x
        # when x == 0, theres 1 way to reach it
        @functools.cache
        def dp(amount):
            if amount == 0:
                return 0
            result = sys.maxsize
            for coin in coins:
                if amount - coin >= 0:
                    result = min(result, 1 + dp(amount - coin))
            return result
            
        return result if (result := dp(amount)) != sys.maxsize else -1