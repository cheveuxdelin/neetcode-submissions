# no negative values
# len(stones) > 1 always?

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a = heapq.heappop(stones)
            b = heapq.heappop(stones)
            difference = abs(a-b)
            if difference > 0:
                heapq.heappush(stones, -difference)
        return -stones[0] if stones else 0
            