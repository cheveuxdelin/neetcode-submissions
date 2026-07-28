# we cant sort
# given the constraints

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            # While the current number is in range [1, n] 
            # AND it is not already sitting at its home index (nums[i] - 1)...
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i]-1]:
                target_idx = nums[i] - 1

                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i+1
        return n+1