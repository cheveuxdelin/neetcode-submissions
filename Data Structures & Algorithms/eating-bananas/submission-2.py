class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def feasible(eating_rate: int) -> bool:
            return sum(math.ceil(pile / eating_rate) for pile in piles) <= h
        
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left