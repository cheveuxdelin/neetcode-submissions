class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        d = defaultdict(int)
        d[0] = 1

        for num in nums:
            next_d = defaultdict(int)
            for currently_in_d in d:
                next_d[currently_in_d+num] += d[currently_in_d]
                next_d[currently_in_d-num] += d[currently_in_d]
            d = next_d
        return d[target]