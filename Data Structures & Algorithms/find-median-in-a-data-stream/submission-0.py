import bisect

class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)
        

    def findMedian(self) -> float:
        # odd
        if len(self.nums) % 2:
            return self.nums[len(self.nums) // 2] + 0.0
        else:
            return (self.nums[len(self.nums) // 2 - 1] + self.nums[len(self.nums) // 2]) / 2