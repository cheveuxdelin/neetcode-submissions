class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(current, i):
            if i == len(nums):
                result.append(current[:])
                return
        
            # skip
            backtrack(current, i+1)
            # include
            current.append(nums[i])
            backtrack(current, i+1)
            current.pop()

        backtrack([], 0)
        return result