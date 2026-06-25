class Solution:
    def isUgly(self, n: int) -> bool:
        x = [2, 3, 5]
        x_i = 0

        while n != 1:
            if not n % x[x_i]:
                n /= x[x_i]
            else:
                x_i += 1
                if x_i == 3:
                    return False
        return True
        