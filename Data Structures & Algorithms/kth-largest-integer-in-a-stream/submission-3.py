class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        for i in range(k, len(nums)):
            heapq.heappushpop(self.heap, nums[i])

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]