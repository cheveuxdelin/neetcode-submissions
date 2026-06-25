class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target, remainder = divmod(sum(nums), 2)
        if remainder:
            return False
        current_set = set([0])

        for num in nums:
            for set_element in list(current_set):
                current_set.add(num+set_element)
        return target in current_set