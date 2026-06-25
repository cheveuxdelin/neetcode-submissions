import itertools

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        values = [(count, element) for element, count in counter.items()]
        heap = values[:k]
        heapq.heapify(heap)

        for count, element in itertools.islice(values, k, None):
            heapq.heappushpop(heap, (count, element))

        return [value[1] for value in heap]