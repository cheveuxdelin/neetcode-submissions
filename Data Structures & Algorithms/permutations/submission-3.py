class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        current_set = set()

        def f():
            if len(current) == len(nums):
                result.append(current[:])
            else:
                for num in nums:
                    if num not in current_set:
                        current.append(num)
                        current_set.add(num)
                        f()
                        current.pop()
                        current_set.discard(num)
        f()
        return result