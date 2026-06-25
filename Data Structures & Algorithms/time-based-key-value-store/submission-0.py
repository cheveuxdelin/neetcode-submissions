class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([int(timestamp), value])

    def get(self, key: str, timestamp: int) -> str:
        array_to_lookup = self.d.get(key)

        if not array_to_lookup:
            return ""
        
        left = 0
        right = len(array_to_lookup)

        while left < right:
            mid = (left + right) // 2
            if array_to_lookup[mid][0] > timestamp:
                right = mid
            else:
                left = mid + 1

        return array_to_lookup[left-1][1] if left > 0 else ""