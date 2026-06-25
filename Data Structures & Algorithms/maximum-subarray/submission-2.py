# negative numbers? zero? afect the outcome
# len(nums) > 0?
# what do we return? THE SUM.
# len(array)??
# podemos utilziar un sliding window y manejar en una pass el numero de currently 
# can the subarray be length zero? NO

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        total = nums[0]

        for num in nums[1:]:
            current = max(current+num, num)
            total = max(current, total)
        return total