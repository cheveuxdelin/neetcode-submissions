class MyCalendar:
    
    def __init__(self):
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        left = 0
        right = len(self.bookings)

        while left < right:
            mid = (left + right) // 2
            if endTime <= self.bookings[mid][0]:
                right = mid
            else:
                left = mid + 1
        
        if left > 0 and startTime < self.bookings[left-1][1]:
            return False

        self.bookings.insert(left, (startTime, endTime))
        return True
        
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)