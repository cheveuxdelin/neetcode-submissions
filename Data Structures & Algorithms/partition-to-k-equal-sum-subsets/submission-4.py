import functools

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        n = len(nums)

        if nums_sum % k:
            return False

        target = nums_sum // k

        @functools.cache
        def backtrack(mask: int, current_sum: int, current_k: int) -> bool:
            if current_k == k - 1:
                return True
            
            for bit in range(mask.bit_length()):
                if (1 << bit) & mask:
                    new_mask = mask
                    new_mask &= ~(1 << bit)
                    new_current_sum = current_sum + nums[bit]

                    if new_current_sum == target and backtrack(new_mask, 0, current_k+1):
                        return True
                    elif new_current_sum < target and backtrack(new_mask, new_current_sum, current_k):
                        return True
            return False

        return backtrack((1 << n) - 1, 0, 0)
