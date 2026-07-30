# insights:
# if you steal house i, you should avoid house i-1
# but you can take house i-2!
# but house i-2, is it the best possible, what about i-3?
# we can find out if we process i-3, then i-2, and then we know we
# can bubble up best possible solution
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return max(nums)

        a = nums[0]
        b = max(a, nums[1])

        for i in range(2, len(nums)):
            c = max(nums[i] + a, b)
            a = b
            b = c
        return c