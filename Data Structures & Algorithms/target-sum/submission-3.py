class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        current = {0: 1}

        for i in range(n):
            next_d = defaultdict(int)
            for total, count in current.items():
                next_d[total+nums[i]] += count
                next_d[total-nums[i]] += count
            current = next_d
        
        return current[target]