class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        counter = collections.Counter(nums)
        d = {}

        result = []
        current = []

        def helper():
            if counter == d:
                result.append(current.copy())
            else:
                for num in counter:
                    if d.get(num, 0) < counter[num]:
                        current.append(num)
                        d[num] = d.get(num, 0) + 1
                        helper()
                        current.pop()
                        d[num] -= 1
        helper()
        return result