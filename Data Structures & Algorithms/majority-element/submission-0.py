class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        result = None

        for num in nums:
            d[num] += 1
            if result is None or d[num] > d[result]:
                result = num
        return result