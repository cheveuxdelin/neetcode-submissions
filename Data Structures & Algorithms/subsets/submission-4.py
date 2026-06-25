class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        current = []
        result = []

        def backtrack(i: int):
            if i == len(nums):
                result.append(current.copy())
            else:
                # skip
                backtrack(i + 1)
                # take
                current.append(nums[i])
                backtrack(i + 1)
                current.pop()

        backtrack(0)
        return result 