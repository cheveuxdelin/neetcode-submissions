class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        current = []

        def f(i):
            if i == len(nums):
                result.append(current[:])
            else:
                # we avoid subsets starting with the same element
                next_index = i
                while next_index < len(nums) and nums[i] == nums[next_index]:
                    next_index += 1

                # skip current
                f(next_index)

                # take current
                current.append(nums[i])
                f(i+1)
                current.pop()
        f(0)
        return result

                

# o (n*2**n+nlog(n))