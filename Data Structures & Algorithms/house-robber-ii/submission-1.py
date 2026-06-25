class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        def max_to_rob(i, j):
            a = nums[i]
            b = max(nums[i], nums[i+1])
            for index in range(i+2, j):
                a, b = b, max(nums[index]+a, b)
            return b
        
        return max(
            max_to_rob(0, len(nums)-1),
            max_to_rob(1, len(nums))
        )
            