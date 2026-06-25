class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = set()

        for num in nums:
            if num not in s:
                s.add(num)
            else:
                s.discard(num)
        return list(s)