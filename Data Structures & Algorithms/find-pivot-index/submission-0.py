# len(array) > 0?
# negative values?
# only one result?
# only numbers?
# size of array?
# number of solutions can be zero

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixes = nums.copy()
        postfixes = nums.copy()

        for i in range(1, len(nums)):
            prefixes[i] += prefixes[i-1]
        for i in range(len(nums)-2, -1, -1):
            postfixes[i] += postfixes[i+1]
        
        for i in range(len(nums)):
            left = prefixes[i-1] if i > 0 else 0
            right = postfixes[i+1] if i < len(nums)-1 else 0
            if left == right:
                return i
        return -1