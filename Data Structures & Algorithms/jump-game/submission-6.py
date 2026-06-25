class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = 0
        j = 1

        while i < j:
            next_j = j
            for index in range(i, j):
                next_j = max(next_j, index+nums[index]+1)
            
            if next_j == j:
                return False
            
            if next_j >= len(nums):
                return True
            
            i = j
            j = next_j
        return False