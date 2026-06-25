
# for most frequenct
# we can use a minheap
# since when minheap is limited by size
# it will get rid of the min value
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = collections.Counter(nums)
        nums = [(count, num) for num, count in frequencies.items()]
        heap = nums[:k]
        heapq.heapify(heap)

        for i in range(k, len(nums)):
            heapq.heappushpop(heap, nums[i])
        
        return [element[1] for element in heap]