class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity: int) -> bool:
            i = 0
            for _ in range(days):
                current_capacity = capacity
                while i < len(weights) and current_capacity >= weights[i]:
                    current_capacity -= weights[i]
                    i += 1
                if i == len(weights):
                    break
            return i == len(weights)
        
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left
                