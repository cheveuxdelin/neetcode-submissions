class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = list(set(nums))
        result = []
        current = []

        def helper(i, s):
            if s == target:
                result.append(current.copy())
            elif s < target and i < len(nums):
                # skip
                helper(i+1, s)
                # take
                current.append(nums[i])
                helper(i, s+nums[i])
                current.pop()
        helper(0, 0)
        return result
