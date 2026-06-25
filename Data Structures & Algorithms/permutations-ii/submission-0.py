class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        count = Counter(nums)

        def dfs():
            if len(current) == len(nums):
                result.append(current.copy())
            else:
                for n in count:
                    if count[n] > 0:
                        current.append(n)
                        count[n] -= 1
                        dfs()
                        count[n] += 1
                        current.pop()
        dfs()
        return result
