import functools
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp(i) = length of the longest increasing subsequence that MUST include nums[i] as the first element
        @functools.cache
        def dp(i: int) -> int:
            lcs = 1

            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    lcs = max(lcs, dp(j)+1)
            return lcs

        return max(dp(i) for i in range(len(nums)))
                    
            