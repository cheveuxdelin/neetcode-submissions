# weird
# but i can see that for each streaming number
# we gotta find the number of days that were less than or equal going back in time
# this is easy if we just append and go back
# but i guess the problem is asking for the compression of solution
# lets first do the naive solution
class StockSpanner:

    def __init__(self):
        self.values = []

    def next(self, price: int) -> int:
        self.values.append(price)
        i = len(self.values)-1
        count = 0

        while i >= 0 and self.values[i] <= price:
            i -= 1
            count += 1
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)