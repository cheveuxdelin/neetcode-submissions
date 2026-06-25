class Solution:
    def findMin(self, nums: List[int]) -> int:
        def condition(candidate):
            return nums[candidate] > nums[right]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if condition(mid):
                left = mid + 1
            else:
                right = mid
        return nums[left]