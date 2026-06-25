class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        dp = [[0] * (capacity+1) for _ in range(len(profit))]

        for c in range(capacity+1):
            if c >= weight[0]:
                dp[0][c] = profit[0]

        for i in range(1, len(profit)):
            for c in range(1, capacity+1):
                # skip
                skipping = dp[i-1][c] # max profit excluding current item
                # take
                taking = profit[i]+dp[i-1][c-weight[i]] if c >= weight[i] else 0
                dp[i][c] = max(skipping, taking)
        return dp[-1][-1]


