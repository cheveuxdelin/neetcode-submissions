import itertools

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        nums = [(value, key) for key, value in counter.items()]

        heap = nums[:k]
        heapq.heapify(heap)

        for num in itertools.islice(nums, k, None):
            heapq.heappushpop(heap, num)
        
        return [num[1] for num in heap]
        