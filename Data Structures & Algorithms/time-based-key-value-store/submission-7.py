class TimeMap:

    def __init__(self):
        self.d = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        
        array = self.d[key]
        left = 0
        right = len(array)

        while left < right:
            mid = (left + right) // 2
            mid_timestamp = array[mid][0]

            if mid_timestamp > timestamp:
                right = mid
            else:
                left = mid + 1
        return array[left-1][1] if left > 0 else ""