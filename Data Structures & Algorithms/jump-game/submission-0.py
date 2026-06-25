class Solution:
    def canJump(self, nums: List[int]) -> bool:
        t = [False] * len(nums)
        t[-1] = True

        for i in range(len(nums)-2, -1, -1):
            for j in range(i+1,min(len(nums), i+1+nums[i])):
                if t[j]:
                    t[i] = True
                    break
        return t[0]