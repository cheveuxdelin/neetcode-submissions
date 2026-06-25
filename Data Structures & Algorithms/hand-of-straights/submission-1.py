class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        c = collections.Counter(hand)
        keys = sorted(c.keys())
        keys_index = 0

        while c:
            next_min = 0
            while not c[keys[keys_index]]:
                keys_index += 1
            min_value = keys[keys_index]

            for i in range(groupSize):
                if not c[min_value+i]:
                    return False
                c[min_value+i] -= 1
                if c[min_value+i] == 0:
                    c.pop(min_value+i)
        return True