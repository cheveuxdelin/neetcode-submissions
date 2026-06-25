# nums > 0?
# solution is 2 *distinct* indices
# we look for elements k away from each other
# there can be no solution (return false)
# depends on indexes, can't sort
# do negatives affect? because there can be (no, it doesnt affect)


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        # we willways keep it size k-1, since we will check the current one as the kth element
        in_range = {}
        for j, num in enumerate(nums):
            # already added
            if num in in_range:
                return True
            
            if len(in_range) == k: #k or k-1?
                in_range.pop(nums[i], None)
                i += 1
            in_range[nums[j]] = j
        return False