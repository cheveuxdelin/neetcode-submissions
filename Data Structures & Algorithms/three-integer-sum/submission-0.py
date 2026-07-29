# no duplicate triplets
# we need to sort in order to do two pointers
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        # to handle duplicates
        # can just discard the nums[i] iteration that is same as nums[i-1] 
        for i in range(len(nums)-2):
            if i == 0 or nums[i] != nums[i-1]:
                # here we want to find pairs of two numbers
                # nums[j] and nums[k]
                # that would be equal to -nums[i]
                # they cancel each other, equals zero

                # there can be multiple pairs(nums[j], nums[k]) within the same i
                j = i+1
                k = len(nums)-1

                while j < k:
                    current_triplet = [nums[i], nums[j], nums[k]]
                    triplet_sum = sum(current_triplet)

                    if triplet_sum == 0:
                        result.append(current_triplet)
                        j += 1
                        k -= 1
                        # to avoid duplicates, we will advance j until its not the same as previous index
                        # accounting for j < k still
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                    # number too low, we move left pointer higher
                    elif triplet_sum < 0:
                        j += 1
                    # number too high, we move right pointer lower
                    else:
                        k -= 1
        return result
                    
