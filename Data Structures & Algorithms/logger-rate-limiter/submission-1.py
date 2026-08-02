class Logger:

    def __init__(self):
        self.last_message_printed = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.last_message_printed or timestamp >= self.last_message_printed[message] + 10:
            self.last_message_printed[message] = timestamp
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
