class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def f(i):
            if i == len(nums):
                result.append(current.copy())
            else:
                # skip
                f(i+1)
                #take
                current.append(nums[i])
                f(i+1)
                current.pop()
        f(0)
        return result