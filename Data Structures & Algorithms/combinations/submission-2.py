class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        current = []

        def backtrack(start_index: int):
            if len(current) == k:
                result.append(current.copy())
            else:
                for i in range(start_index, n+1):
                    current.append(i)
                    backtrack(i+1)
                    current.pop()
        backtrack(1)
        return result