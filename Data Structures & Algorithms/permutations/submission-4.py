class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        result = []
        current = []

        def f():
            if len(current) == len(nums):
                result.append(current.copy())
            else:
                for num in nums:
                    if num not in visited:
                        visited.add(num)
                        current.append(num)
                        f()
                        visited.discard(num)
                        current.pop()
        f()
        return result