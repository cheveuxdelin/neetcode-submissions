class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0

        for i in range(32):
            bit = bool(n & (1 << i))
            result |= bit << (31 - i)
        return result