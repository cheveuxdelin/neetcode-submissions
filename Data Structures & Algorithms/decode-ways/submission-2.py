from functools import cache

class Solution:

    def numDecodings(self, s: str) -> int:

        @cache
        def f(i):
            if i == len(s):
                return 1
            else:
                value = 0
                if s[i] != "0":
                    value += f(i+1)
                    if i < len(s)-1 and int(s[i:i+2]) <= 26:
                        value += f(i+2)
                return value

        return f(0)