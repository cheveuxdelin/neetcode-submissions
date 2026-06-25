class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def backtrack(i):
            if i == len(nums):
                result.append(current[:])
            else:
                # skip current
                backtrack(i+1)

                # take current
                current.append(nums[i])
                backtrack(i+1)
                current.pop()
        backtrack(0)
        return result

                