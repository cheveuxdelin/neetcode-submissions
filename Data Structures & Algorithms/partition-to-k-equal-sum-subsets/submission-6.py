import functools

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums_sum = sum(nums)
        n = len(nums)

        if nums_sum % k:
            return False

        nums.sort(reverse=True)
        target = nums_sum // k

        # memo only for mask, since all other values are derived
        memo = {}

        @functools.cache
        def backtrack(mask: int, current_sum: int, current_k: int, start_index: int) -> bool:
            if current_k == k - 1:
                return True
            
            if mask in memo:
                return memo[mask]
            
            for bit in range(start_index, n):
                if (1 << bit) & mask:
                    new_mask = mask & ~(1 << bit)
                    new_current_sum = current_sum + nums[bit]

                    if new_current_sum == target and backtrack(new_mask, 0, current_k+1, 0):
                        memo[mask] = True
                        return memo[mask]
                    elif new_current_sum < target and backtrack(new_mask, new_current_sum, current_k, bit+1):
                        memo[mask] = True
                        return memo[mask]
            memo[mask] = False
            return False

        return backtrack((1 << n) - 1, 0, 0, 0)
