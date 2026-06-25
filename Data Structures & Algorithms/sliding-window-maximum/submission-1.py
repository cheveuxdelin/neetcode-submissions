class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i = 0
        deque = collections.deque()
        result = []

        for j, c in enumerate(nums):
            while deque and nums[deque[-1]] < c:
                deque.pop()
            deque.append(j)

            if i > deque[0]:
                deque.popleft()
            
            if j >= k - 1:
                result.append(nums[deque[0]])
                i += 1
        return result