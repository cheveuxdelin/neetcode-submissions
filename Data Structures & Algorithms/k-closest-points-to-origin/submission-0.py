class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculate_distance(x, y):
            return x*x + y*y
        
        heap = []
        for x, y in points:
            heapq.heappush(heap, (calculate_distance(x, y), (x, y)))
        
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result