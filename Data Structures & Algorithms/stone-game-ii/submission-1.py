from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        prefix = [0] * (len(piles)+1)

        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] + piles[i-1]

        @cache
        def f(i, m, alice_turn):
            if i >= len(piles):
                return 0
            else:
                if alice_turn:
                    result = 0
                    for x in range(2*m):
                        if i+x >= len(piles):
                            break
                        taken = prefix[i+x+1] - prefix[i]
                        candidate = f(i+x+1, max(x+1, m), not alice_turn)
                        if taken + candidate > result:
                            result = taken + candidate
                    return result
                else:
                    result = sys.maxsize
                    for x in range(m*2):
                        if i+x >= len(piles):
                            break
                        candidate = f(i+x+1, max(x+1, m), not alice_turn)
                        if candidate < result:
                            result = candidate
                    return result
        return f(0, 1, True) 
