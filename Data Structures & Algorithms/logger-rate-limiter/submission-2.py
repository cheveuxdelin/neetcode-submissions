class Logger:

    def __init__(self):
        self.last_time_printed = collections.defaultdict(lambda: -10)
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp - 10 >= self.last_time_printed[message]:
            self.last_time_printed[message] = timestamp
            return True
        return False


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
