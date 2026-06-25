class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for previous in range(i):
                if nums[previous] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[previous])
        return max(dp)