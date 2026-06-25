class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for i in range(groupSize):
                if first+i not in count:
                    return False
                count[first+i] -= 1
                if count[first+i] == 0:
                    heapq.heappop(min_heap)
        return True