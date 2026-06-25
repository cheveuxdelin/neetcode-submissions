class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        left = right = 0

        while right < len(nums) - 1:
            next_left = right + 1
            for i in range(left, right+1):
                right = max(right, i+nums[i])
            left = next_left
            res += 1
        return res