# we're looking for the minimum index where
# nums[mid] < nums[(mid+1) % n]

# i think we will also again be needing to find the sorted part
# or not?
# since we use modulus maybe we avoid that

# new approach, the minimum has to be in the unordered section!!!
# we keep looking for the unordered section
# and we will end up finding a number that is something
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid + 1
        return nums[left]
