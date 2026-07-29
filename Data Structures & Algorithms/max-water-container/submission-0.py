class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        result = 0

        def calculate_area(a, b):
            return min(heights[a], heights[b]) * (b - a)

        while left < right:
            result = max(result, calculate_area(left, right))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result