# this has no ordering, so how can i solve?
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # we need only to find a local maximum
        # a local maximum would be closing the gap between going uphill and going downhill
        # on any hill

        # there will always be a peak
        # that means that if we end up being at any border,
        # we can just finish,
        # since the solution space was exhausted to be forced the solution to be in the borders
        # we dont have to do anything about this, since mid being in the border would mean
        # left and right have already converged to same index
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            # we dont wanna go further to the right in the search
            # since either mid or to the left or mid we find the peak
            # this is told by mid+1 being lower than mid
            if nums[mid] >= nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left
            
