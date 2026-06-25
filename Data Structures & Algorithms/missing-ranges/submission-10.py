class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        result = []
        
        if lower < nums[0]:
            result.append([lower, nums[0]-1])
        if upper > nums[-1]:
            nums.append(upper+1)
        

        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                result.append([nums[i]+1, nums[i+1]-1])
        return result