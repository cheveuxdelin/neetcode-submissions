# cyclic sort
# for every number that you encounter,
# you need to check a function is_in_target(num: int)
# where its output will be, the respective position of a number, given its value
# target_index(num: int) = num - 1

# since its 1..n instead of 0..n-1, all numbers are transposed on +1
# so we substract it in the target_index variable
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            target_index = nums[i]-1
            while nums[i] != nums[target_index]:
                nums[i], nums[target_index] = nums[target_index], nums[i]
                target_index = nums[i]-1
        
        result = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                result.append(i+1)
        return result