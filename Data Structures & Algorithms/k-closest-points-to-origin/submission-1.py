class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_to_origin(point):
            return point[0]**2 + point[1]**2
        
        heap = [(-distance_to_origin(points[i]), points[i]) for i in range(k)]
        heapq.heapify(heap)
        for i in range(k, len(points)):
            heapq.heappushpop(heap, (-distance_to_origin(points[i]), points[i]))
        
        return sorted([d[1] for d in heap])
