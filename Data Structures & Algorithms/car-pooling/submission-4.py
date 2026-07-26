import typing
# this can be event based
# but for sake of practicing heaps,
# lets simulate the ride


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # (end_time, n_passengers)
        awaiting_destination = collections.deque()
        current_capaciy = 0

        # we sort by destination
        trips.sort(key=lambda x: x[1])

        for trip in trips:
            while awaiting_destination and trip[1] >= awaiting_destination[0][0]:
                arrived = awaiting_destination.popleft()
                current_capaciy -= arrived[1]

            awaiting_destination.append((trip[2], trip[0]))
            current_capaciy += trip[0]
            if current_capaciy > capacity:
                return False
        return True
