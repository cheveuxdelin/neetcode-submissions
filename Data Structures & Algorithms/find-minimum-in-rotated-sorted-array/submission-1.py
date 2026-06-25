class Solution:
    def findMin(self, nums: List[int]) -> int:
        def condition(candidate):
            return nums[candidate] > nums[right]

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if not condition(mid):
                right = mid
            else:
                left = mid + 1
        return nums[left]