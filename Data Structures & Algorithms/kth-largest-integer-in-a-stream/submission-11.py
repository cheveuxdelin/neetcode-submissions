# for finding the kth largest, we need min_heap
# heapq
import heapq
# no more notes
# what if there's less than k elements and its asking for k?
# its guaranteed that this will never be the case based on constraints

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # initialization can be both smaller or >= k
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)        

    def add(self, val: int) -> int:
        operation = heapq.heappush if len(self.heap) < self.k else heapq.heappushpop
        operation(self.heap, val)
        return self.heap[0]