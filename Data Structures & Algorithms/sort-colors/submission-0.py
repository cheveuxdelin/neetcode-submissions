class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]

        i = 0
        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(right, i)
                right -= 1
                i -= 1
            i += 1
        