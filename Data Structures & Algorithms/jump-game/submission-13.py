class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        j = 0

        while True:
            max_next_jump = j
            for index in range(i, j+1):
                max_next_jump = max(max_next_jump, index+nums[index])

            if max_next_jump >= len(nums)-1:
                return True
            elif max_next_jump == j:
                return False
            else:
                i = j+1
                j = max_next_jump


