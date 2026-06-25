import functools
import collections

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {0: 1}

        for num in nums:
            next_dp = collections.defaultdict(int)
            for element in dp:
                next_dp[element+num] += dp[element]
                next_dp[element-num] += dp[element]
            dp = next_dp
        return dp[target]