class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        heap = []

        for key in counter:
            heapq.heappush(heap, key)
        
        while counter:
            while heap and heap[0] not in counter:
                heapq.heappop(heap)
            next_min = heap[0]
            if counter[next_min] == 1:
                heapq.heappop(heap)

            for i in range(groupSize):
                if next_min+i not in counter:
                    return False
                counter[next_min+i] -= 1
                if counter[next_min+i] == 0:
                    counter.pop(next_min+i)
        return True

