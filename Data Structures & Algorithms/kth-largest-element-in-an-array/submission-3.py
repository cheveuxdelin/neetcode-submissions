class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for value in islice(nums, k, None):
            heapq.heappushpop(heap, value)
        return heap[0]