class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        rtn = []
        visited = set()

        def backtrack(p):
            if len(p) == len(nums):
                rtn.append(p[:])
            else:
                for num in nums:
                    if num not in visited:
                        visited.add(num)
                        p.append(num)
                        backtrack(p)
                        p.pop()
                        visited.discard(num)
        backtrack([])
        return rtn