class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def helper(i):
            if i == len(nums):
                result.append(current.copy())
            else:
                # skip
                helper(i+1)
                # take
                current.append(nums[i])
                helper(i+1)
                current.pop()
        
        helper(0)
        return result