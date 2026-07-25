# weird
# but i can see that for each streaming number
# we gotta find the number of days that were less than or equal going back in time
# this is easy if we just append and go back
# but i guess the problem is asking for the compression of solution
# lets first do the naive solution

# now lets think on the optimized solution
# if we have it, instead of free fluctuating sizes like a skyline,
# we have a strictly decreasing values
# we dont have to iterate the whole array if we have that

price_index = 0
n_bigger_than = 1
class StockSpanner:

    def __init__(self):
        # (price, n_bigger_than)
        self.values = []

    def next(self, price: int) -> int:
        # since we start from today, we inititalize at 1 instead of 0
        count = 1
        # we pop/accumulate and compress past results
        while self.values and price >= self.values[-1][price_index]:
            count += self.values.pop()[n_bigger_than]
        
        self.values.append((price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)