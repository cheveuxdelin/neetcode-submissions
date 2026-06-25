class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        current_set = set()

        def backtrack():
            if len(current) == len(nums):
                result.append(current.copy())
            else:
                for num in nums:
                    if num not in current_set:
                        current_set.add(num)
                        current.append(num)
                        backtrack()
                        current_set.discard(num)
                        current.pop()
        backtrack()
        return result