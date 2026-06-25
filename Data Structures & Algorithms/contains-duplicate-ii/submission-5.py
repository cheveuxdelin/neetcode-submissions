class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        d = set()
        for j in range(len(nums)):
            if nums[j] in d:
                return True
            
            d.add(nums[j])
            if j >= k:
                d.discard(nums[i])
                i += 1
        return False