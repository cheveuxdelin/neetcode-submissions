# checking if nums[0] > nums[-1] tell us if its rotated, but is that helpful at all?
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # given a midpoint,
        # either the start of the array to midpoint is going to be sorted
        # or midpoint to the end is going to be sorted
        # find the sorted section.
        # having recognized the range of sorted values,
        # if target in the sorted range:
        # go into that range
        # if not, we know it is in the unsorted part
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            
            # left sorted portion
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1