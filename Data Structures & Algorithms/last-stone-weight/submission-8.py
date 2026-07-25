# heap again, nothing crazy
# we need to be having a max heap
# iterate and just follow the instructions
# there can be 1 or zero stones remaining
# since we do have to look for the two heaviest stones,
# theres no O(N*logK) optimization possible
# it ends up being the same as sorting really, and working sorted, in complexity
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            a, b = heapq.heappop(heap), heapq.heappop(heap)
            if a != b:
                heapq.heappush(heap, a - b)
        return -heap[0] if len(heap) else 0
        