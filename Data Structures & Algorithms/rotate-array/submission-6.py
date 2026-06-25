class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        def rotate_by_one():
            tmp = nums[-1]
            for i in range(len(nums)):
                nums[i], tmp = tmp, nums[i]
                
        for _ in range(k):
            rotate_by_one()

                
