class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_to_origin(point):
            return point[0]**2 + point[1]**2
        
        heap = [(-distance_to_origin(point), point) for point in islice(points, k)]
        heapq.heapify(heap)

        for point in islice(points, k, None):
            heapq.heappushpop(heap, (-distance_to_origin(point), point))
        
        return [value[1] for value in heap]