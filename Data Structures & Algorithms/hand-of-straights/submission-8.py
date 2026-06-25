class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        heap = []

        for key in counter:
            heapq.heappush(heap, key)
        
        while heap:
            while heap and heap[0] not in counter:
                heapq.heappop(heap)
            if not heap:
                break
            
            next_min = heap[0]
            for i in range(groupSize):
                current_index = next_min+i
                if current_index not in counter:
                    return False
                counter[current_index] -= 1
                if counter[current_index] == 0:
                    counter.pop(current_index)
        return True

