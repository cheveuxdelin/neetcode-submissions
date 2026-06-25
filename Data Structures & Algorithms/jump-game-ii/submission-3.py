class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        j = 1
        number_of_jumps = 0

        while j < len(nums):
            next_frontier = j
            for index in range(i, j):
                next_frontier = max(next_frontier, index+nums[index])
            i = j
            j = next_frontier + 1
            number_of_jumps += 1
        return number_of_jumps