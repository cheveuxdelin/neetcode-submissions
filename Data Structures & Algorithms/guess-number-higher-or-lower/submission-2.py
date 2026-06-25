# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# can 
class Solution:
    def guessNumber(self, n: int) -> int:
        equal = 0
        higher = -1
        lower = 1

        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == equal:
                return mid
            # higher meaning my guess was higher than num
            # means we have to go lower
            elif result == higher:
                right = mid
            # lower meaning my gues was lower than the num
            # we have to look into higher values
            else:
                left = mid + 1
        return left