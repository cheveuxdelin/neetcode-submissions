import itertools

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]

        result = []

        # from starting to the first element in the array
        if nums[0] != lower:
            result.append([lower, nums[0]-1])

        # in-between
        last = nums[0]
        for current in itertools.islice(nums, 1, None):
            if current != last+1:
                result.append([last+1, current-1])
            last = current

        # from ending index to the upper bound
        if nums[-1] != upper:
            result.append([nums[-1]+1, upper])
        return result