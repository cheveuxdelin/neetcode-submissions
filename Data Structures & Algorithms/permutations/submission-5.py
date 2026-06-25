class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        current_set = set()

        def helper(i):
            if len(current) == len(nums):
                result.append(current.copy())
            elif i < len(nums):
                # skip
                helper(i + 1)
                # take
                if nums[i] not in current_set:
                    current_set.add(nums[i])
                    current.append(nums[i])
                    helper(0)
                    current_set.discard(nums[i])
                    current.pop()
        helper(0)
        return result