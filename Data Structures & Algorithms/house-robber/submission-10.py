import functools

class Solution:
    def rob(self, nums: List[int]) -> int:
        @functools.cache
        def backtrack(i: int) -> int:
            if i >= len(nums):
                return 0
            return max(
                nums[i] + backtrack(i+2),
                backtrack(i+1)
            )
        return backtrack(0)