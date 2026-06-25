class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        i = 0
        j = 1

        while j < len(nums):
            next_j = j
            for index in range(i, j):
                next_j = max(next_j, index+nums[index]+1)
            i = j
            j = next_j
            count += 1
        return count