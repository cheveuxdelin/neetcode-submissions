class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        next_index_not_val = 0

        for num in nums:
            if num != val:
                nums[next_index_not_val] = num
                next_index_not_val += 1
        return next_index_not_val