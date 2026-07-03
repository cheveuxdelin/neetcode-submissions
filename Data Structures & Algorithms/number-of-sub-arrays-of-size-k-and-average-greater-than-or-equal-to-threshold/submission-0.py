class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        i = 0
        current = 0

        for j in range(len(arr)):
            current += arr[j]

            if j >= k:
                current -= arr[i]
                i += 1
            if j >= k-1:
                result += (current / k) >= threshold
        return result
                