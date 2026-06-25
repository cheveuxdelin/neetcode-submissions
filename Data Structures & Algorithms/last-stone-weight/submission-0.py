class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # o(n)
        heap = [-stone for stone in stones]
        # o(n)
        heapq.heapify(heap)

        while len(heap) >= 2:
            # o(log n))
            first_stone = heapq.heappop(heap)
            # o(log(n))
            second_stone = heapq.heappop(heap)
            new_weight = abs(first_stone - second_stone)
            if new_weight != 0:
                # o(log(n))
                heapq.heappush(heap, -new_weight)
        return -heap[0] if len(heap) == 1 else 0