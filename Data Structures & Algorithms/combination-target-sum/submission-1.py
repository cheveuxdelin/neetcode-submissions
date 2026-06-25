class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i, current, total):
            if total == target:
                result.append(current[:])
            elif i < len(nums) and total < target:
                backtrack(i+1, current, total)
                current.append(nums[i])
                backtrack(i, current, total+nums[i])
                current.pop()
        backtrack(0, [], 0)
        return result