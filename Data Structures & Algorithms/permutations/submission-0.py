class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rtn = []

        def backtrack(p):
            if len(p) == len(nums):
                rtn.append(p[:])
            else:
                for num in nums:
                    if num not in p:
                        p.append(num)
                        backtrack(p)
                        p.pop()
        backtrack([])
        return rtn