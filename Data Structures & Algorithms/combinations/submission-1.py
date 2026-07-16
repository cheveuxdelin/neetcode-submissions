class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        current = []

        def helper(i: int):
            if len(current) == k:
                result.append(current.copy())
            elif i <= n:
                for j in range(i, n+1):
                    current.append(j)
                    helper(j+1)
                    current.pop()
        helper(1)
        return result