import functools

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        processed_strs = [(s.count("0"), s.count("1")) for s in strs]

        @functools.cache
        def dp(remaining: tuple[int, int], i: int) -> int:
            if i == len(processed_strs):
                return 0
            
            # skipping
            best = dp(remaining, i+1)

            # taking
            candidate = processed_strs[i]
            next_state = (remaining[0]-candidate[0], remaining[1]-candidate[1])
            if all(num >= 0 for num in next_state):
                best = max(best, 1 + dp(next_state, i+1))
            return best
        return dp((m,n), 0)