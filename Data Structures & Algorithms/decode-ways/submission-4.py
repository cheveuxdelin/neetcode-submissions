import functools

class Solution:
    def numDecodings(self, s: str) -> int:
        @functools.cache
        def helper(i):
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == "0":
                return 0
            
            result = 0
            result += helper(i+1)
            if int(s[i:i+2]) <= 26:
                result += helper(i+2)
            return result
            
            
        
        return helper(0)