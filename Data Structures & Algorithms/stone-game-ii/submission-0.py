from functools import cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def f(i, m, alice_turn):
            if i >= len(piles):
                return 0
            else:
                if alice_turn:
                    current = 0
                    result = 0
                    for x in range(2*m):
                        if i+x >= len(piles):
                            break
                        current += piles[i+x]
                        candidate = f(i+x+1, max(x+1, m), not alice_turn)
                        if current + candidate > result:
                            result = current+candidate
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
