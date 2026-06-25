class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        values = [-value for value in stones]
        heapq.heapify(values)

        while len(values) >= 2:
            rock1 = -heapq.heappop(values)
            rock2 = -heapq.heappop(values)
            if rock1 != rock2:
                heapq.heappush(values, -(rock1 - rock2))
        return -values[0] if values else 0

