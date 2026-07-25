# heap
# nothing crazy, just compute the distance for each points
# and then maintain a min_heap to find the smallest values
# since we dont care about the order of these k smallest values
# its what makes heap a better no-doubt approach than just sorting
# and then slicing the sorted array
# because ordering between these, dont matter

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin = [0, 0]
        def calculate_distance(point1, point2):
            return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
        
        min_heap = []
        for point in points:
            operation = heapq.heappush if len(min_heap) < k else heapq.heappushpop
            distance = calculate_distance(origin, point)
            operation(min_heap, (-distance, point))
        return [point for _, point in min_heap]