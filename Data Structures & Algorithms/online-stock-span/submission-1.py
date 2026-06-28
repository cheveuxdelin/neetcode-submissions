class StockSpanner:

    def __init__(self):
        # span_length, value
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][1] <= price:
            span_length, _ = self.stack.pop()
            span += span_length
        self.stack.append((span, price))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)