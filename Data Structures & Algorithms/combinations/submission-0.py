class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def f(i, current):
            if len(current) == k:
                result.append(current[:])
            elif i <= n:
                # skip
                f(i+1, current)

                # take
                current.append(i)
                f(i+1, current)
                current.pop()
        f(1, [])
        return result