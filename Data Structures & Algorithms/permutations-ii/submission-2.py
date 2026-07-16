class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        counter = collections.Counter(nums)
        result = []
        current = []

        def helper():
            if len(current) == len(nums):
                result.append(current.copy())
            else:
                for num in counter:
                    if counter[num] != 0:
                        counter[num] -= 1
                        current.append(num)
                        helper()
                        counter[num] += 1
                        current.pop()
        helper()
        return result