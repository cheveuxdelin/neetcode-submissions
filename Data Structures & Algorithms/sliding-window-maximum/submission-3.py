class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque = collections.deque()
        result = []

        for i, c in enumerate(nums):
            while deque and nums[deque[-1]] < c:
                deque.pop()
            deque.append(i)

            if deque[0] <= i - k:
                deque.popleft()
            
            if i >= k - 1:
                result.append(nums[deque[0]])
        return result