class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(current, s, i):
            if s == target:
                result.append(current[:])
            elif s < target and i < len(nums):
                backtrack(current, s, i+1)
                current.append(nums[i])
                backtrack(current, s+nums[i], i)
                current.pop()
        backtrack([], 0, 0)
        return result