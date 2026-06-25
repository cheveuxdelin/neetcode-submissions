from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def f(remaining):
            if remaining == 0:
                return 0
            else:
                result = sys.maxsize
                for coin in coins:
                    if coin <= remaining:
                        result = min(result, 1+f(remaining-coin))
                return result
        return min_coins if (min_coins := f(amount)) != sys.maxsize else -1