class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # f(i) = longest increasing subsequence starting from index i
        def f(i):
            if i == len(nums)-1:
                return 1
            else:
                max_length = 1

                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j]:
                        max_length = max(max_length, 1 + f(j))
                return max_length
        return max(f(i) for i in range(len(nums)))