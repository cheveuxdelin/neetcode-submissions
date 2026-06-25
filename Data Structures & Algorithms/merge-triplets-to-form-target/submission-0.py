class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def is_greater(triplet):
            return triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]
        
        current = [1, 1, 1]
        for triplet in triplets:
            if not is_greater(triplet):
                current = [
                    max(current[0], triplet[0]),
                    max(current[1], triplet[1]),
                    max(current[2], triplet[2]),
                ]
        return current == target