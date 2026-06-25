class TimeMap:
    def __init__(self):
        self.d = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if (arr := self.d.get(key)):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid][0] > timestamp:
                    right = mid
                else:
                    left = mid + 1
            
            if left > 0:
                return arr[left - 1][1]
        return ""
        
