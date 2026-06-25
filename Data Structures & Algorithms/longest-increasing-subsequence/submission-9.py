import functools

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # f(i) = longest increasing subsequence starting from index i
        @functools.cache
        def f(i):
            if i == len(nums)-1:
                return 1
            else:
                max_length = 1

                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j]:
                        max_length = max(max_length, 1 + f(j))
                return max_length
        return max(f(i) for i in range(len(nums)))

        ###########################
        dp = [1] * len(nums)

        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
