import functools
# completion will mean finishing them all
# we can move an index forward and have a current_sum
# since multiple paths can lead to the same index and same current_sum
# we are able to dp
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @functools.cache
        def helper(i: int, current_sum: int):
            if i == len(nums):
                return current_sum == target
            else:
                # two paths,
                # one substracting
                # another adding
                return helper(i+1, current_sum+nums[i]) + helper(i+1, current_sum-nums[i])
        return helper(0, 0)