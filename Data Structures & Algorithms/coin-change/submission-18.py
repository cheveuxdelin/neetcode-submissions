import functools
class Solution:
    # whats the intuition behind passing remaining instead of 0?

    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp(remaining) = minimum number of coins to complete remaining
        @functools.cache
        def dp(remaining: int) -> int:
            if remaining == 0:
                return 0
            min_coins_needed = sys.maxsize
            for coin in coins:
                if remaining - coin >= 0:
                    min_coins_needed = min(min_coins_needed, 1 + dp(remaining-coin))
            return min_coins_needed
        
        result = dp(amount)
        return result if result != sys.maxsize else -1
