class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        current = 0

        for num in nums:
            if current == 0:
                candidate = num
            current += 1 if num == candidate else -1
        return candidate
