import functools

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @functools.cache
        def f(remaining):
            if remaining == 0:
                return 0
            else:
                result = sys.maxsize
                for coin in coins:
                    if (candidate := remaining-coin) >= 0:
                        result = min(result, 1+f(candidate))
                return result
        return result if (result := f(amount)) != sys.maxsize else -1