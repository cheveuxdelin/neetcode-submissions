class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_of_nums = sum(nums)
        if sum_of_nums % 2:
            return False
        target = sum_of_nums // 2

        current_set = set((0,))

        for num in nums:
            next_set = set(current_set)
            for element_in_set in current_set:
                next_set.add(element_in_set+num)
            next_set.add(num)
            current_set = next_set
        return target in current_set

