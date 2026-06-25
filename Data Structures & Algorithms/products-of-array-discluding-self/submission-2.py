class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ltr = [1] * len(nums)
        rtl = [1] * len(nums)

        for i in range(1, len(nums)):
            ltr[i] = ltr[i-1] * nums[i-1]
        for i in range(len(nums) - 2, -1, -1):
            rtl[i] = rtl[i+1] * nums[i+1]
        
        return [ltr[i] * rtl[i] for i in range(len(nums))]
