class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = collections.Counter(hand)

        while c:
            min_value = min(c.keys())
            for i in range(groupSize):
                if not c[min_value+i]:
                    return False
                c[min_value+i] -= 1
                if c[min_value+i] == 0:
                    c.pop(min_value+i)
        return True