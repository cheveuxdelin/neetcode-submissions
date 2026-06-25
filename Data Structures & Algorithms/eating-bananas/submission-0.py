class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(candidate):
            remaining_hours = h
            for pile in piles:
                remaining_hours -= math.ceil(pile / candidate)
                if remaining_hours < 0:
                    return False
            return True
            
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left