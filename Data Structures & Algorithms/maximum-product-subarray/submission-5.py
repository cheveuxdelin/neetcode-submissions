class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        cur_min = 1
        cur_max = 1

        for num in nums:
            tmp = cur_max * num
            cur_max = max(cur_min*num, cur_max*num, num)
            cur_min = min(cur_min*num, tmp, num)
            res = max(res, cur_max)
        return res