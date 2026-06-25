class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums:
            next_dp = defaultdict(int)
            for key, count in dp.items():
                next_dp[key-num] += count
                next_dp[key+num] += count
            dp = next_dp
        return dp[target]