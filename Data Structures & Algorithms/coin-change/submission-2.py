from functools import cache

class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        # f(n) = min(f(n-coin) coin in coins if n - coin >= 0)

        @cache
        def f(remaining):
            if remaining == 0:
                return 0
            
            elif remaining > 0:
                min_coins = math.inf
                for coin in coins:
                    if remaining >= coin:
                        min_coins = min(min_coins, 1 + f(remaining-coin))
                return min_coins
        
        result = f(amount)

        if result == math.inf:
            return -1
        
        return result