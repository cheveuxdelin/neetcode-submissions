class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        end = 0
        passenger = 1

        trips.sort(key=lambda x:x[1])
        heap = []
        c = 0
        for n_passengers, current_start, current_end in trips:
            while heap and heap[0][end] <= current_start:
                c -= heapq.heappop(heap)[passenger]
            c += n_passengers
            if c > capacity:
                return False
            heapq.heappush(heap, (current_end, n_passengers))
        return True