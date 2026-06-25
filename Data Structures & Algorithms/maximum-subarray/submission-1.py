# negative numbers? zero? afect the outcome
# len(nums) > 0?
# what do we return? THE SUM.
# len(array)??
# podemos utilziar un sliding window y manejar en una pass el numero de currently 
# can the subarray be length zero? NO

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = -sys.maxsize
        total = -sys.maxsize

        for num in nums:
            current = max(current+num, num)
            total = max(current, total)
        return total