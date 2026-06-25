import functools

class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        @functools.cache
        def f(i, remaining):
            if i == len(profit):
                return 0
            else:
                # skip
                skipping = f(i+1, remaining)
                # take
                taking = 0
                if remaining >= weight[i]:
                    taking = profit[i] + f(i+1, remaining-weight[i])
                return max(skipping, taking)
        return f(0, capacity)

