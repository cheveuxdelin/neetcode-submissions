# what i see:
# we preserve the order,
# so we can only iterate forwards
# we will need an index of starting point
# multiple past indexes can reach a given index
# this means there is repeated work
# whats a base case i can think of???

# for the first index, longest increasing subsequence is itself
# and for each of them, its gonna be at least one
# since one index depends on the [0, index-1], we should be calculating this range (?)
# yes. because what if index+1 is lower than index? you cant really use it
# what you can be storing is the max for a past index
# thats where the optimization comes from, you will still need to see them all

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                # correctness check: we gotta be bigger than the previous
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        # i know whats happening, dp[i] here means, including the current index
        # but what if the last index is not the longest subsequence?
        # it doesnt necessarily need to include it
        # return dp[-1]
        return max(dp)