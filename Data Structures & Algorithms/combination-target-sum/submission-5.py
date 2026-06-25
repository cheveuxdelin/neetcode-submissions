class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(i: int, current: int, p: list[int]):
            if current == target:
                result.append(p.copy())
            elif i < len(nums) and current < target:
                # skip
                backtrack(i+1, current, p)
                # take
                current += nums[i]
                p.append(nums[i])
                backtrack(i, current, p)
                current -= nums[i]
                p.pop()
        backtrack(0, 0, [])
        return result