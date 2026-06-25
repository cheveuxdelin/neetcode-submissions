class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums[:k]
        self.k = k
        heapq.heapify(self.heap)

        for i in range(k, len(nums)):
            heapq.heappushpop(self.heap, nums[i])

    def add(self, val: int) -> int:
        operation = heapq.heappush if len(self.heap) < self.k else heapq.heappushpop
        operation(self.heap, val)
        return self.heap[0]