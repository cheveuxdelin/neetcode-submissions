class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passenger_change = [0] * 1001

        for n_passengers, start, end in trips:
            passenger_change[start] += n_passengers
            passenger_change[end] -= n_passengers
        
        current = 0
        for c in passenger_change:
            current += c
            if current > capacity:
                return False
        return True