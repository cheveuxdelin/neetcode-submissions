# len(nums) > 0?
# all nums are positive?
# is there a solution?
# we return length

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        result = sys.maxsize
        current = 0

        for j, num in enumerate(nums):
            current += num
            while i <= j and current >= target:
                current -= nums[i]
                result = min(result, j-i+1)
                i += 1
        return result if result != sys.maxsize else 0