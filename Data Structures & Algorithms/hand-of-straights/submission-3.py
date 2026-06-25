class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)

        while counter:
            min_key = min(counter.keys())
            for i in range(groupSize):
                if min_key+i not in counter:
                    return False
                counter[min_key+i] -= 1
                if counter[min_key+i] == 0:
                    counter.pop(min_key+i)
        return True
