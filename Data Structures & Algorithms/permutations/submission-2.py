class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []

        def f():
            if len(current) == len(nums):
                result.append(current[:])
            else:
                for num in nums:
                    if num not in current:
                        current.append(num)
                        f()
                        current.pop()
        f()
        return result