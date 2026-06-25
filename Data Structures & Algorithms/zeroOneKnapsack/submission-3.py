class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        current = [0] * (capacity+1)
        for c in range(capacity+1):
            if c >= weight[0]:
                current[c] = profit[0]

        for i in range(1, len(profit)):
            for c in range(capacity, -1, -1):
                # skip
                skipping = current[c] # max profit excluding current item
                # take
                taking = profit[i]+current[c-weight[i]] if c >= weight[i] else 0
                current[c] = max(skipping, taking)
        return current[-1]


