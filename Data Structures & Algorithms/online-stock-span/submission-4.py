import typing

class PriceItem(typing.NamedTuple):
    price: int
    n_smaller_than: int

class StockSpanner:

    def __init__(self):
        # (price, n_bigger_than)
        self.values = []

    def next(self, price: int) -> int:
        # since we start from today, we inititalize at 1 instead of 0
        count = 1
        # we pop/accumulate and compress past results
        while self.values and price >= self.values[-1].price:
            count += self.values.pop().n_smaller_than
        
        self.values.append(PriceItem(price, count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)