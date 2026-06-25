class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        j = 1

        while j < len(nums):
            next_j = j
            for index in range(i, j):
                next_j = max(next_j, index+nums[index]+1)
            if next_j == j:
                return False
            i = j
            j = next_j
        return True