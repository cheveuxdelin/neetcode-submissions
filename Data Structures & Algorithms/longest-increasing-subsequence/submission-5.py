class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def f(current, previous):
            if current == len(nums):
                return 0
            
            lis = f(current+1, previous)

            if previous is None or nums[previous] < nums[current]:
                lis = max(lis, 1 + f(current+1, current))
            
            return lis
        return f(0, None)