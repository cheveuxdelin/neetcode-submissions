class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        lcs_length = 0

        for num in nums_set:
            if num-1 not in nums_set:
                i = 0
                while num+i in nums_set:
                    i += 1
                lcs_length = max(lcs_length, i)
        return lcs_length