class Solution:
    def helper(self, p: list[int]) -> int:
        if len(p) == 1:
            return p[0]
        dp = [0] * len(p)
        dp[0] = p[0]
        dp[1] = max(p[0], p[1])

        for i in range(2, len(p)):
            dp[i] = max(p[i]+dp[i-2], dp[i-1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(
            self.helper(nums[1:]),
            self.helper(nums[:-1])
        )