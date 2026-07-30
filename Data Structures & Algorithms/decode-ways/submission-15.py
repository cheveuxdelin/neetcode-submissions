# import functools

# class Solution:
#     def numDecodings(self, s: str) -> int:
#         # dp(i) = starting from i, number of ways you can decode the rest of the string
#         # an empty string has no way of decding, so 
#         # every individual decision will add a new way of decoding it
#         # but what if we are not able to reach the end? "0" can be a sinkhole
#         # we can instead check correctness and be counting if we are able to reach the end
#         # and we define the base case that an empty string is actually a valid decoding
#         # theres only a valid way to decode an empty string, another empty string
#         # we count the numbre of times we can reach the end
#         # dp(i) => number of ways we can decode s[i:]
#         @functools.cache
#         def dp(i: int) -> int:
#             if i >= len(s):
#                 return 1
#             elif s[i] == "0":
#                 return 0
#                 # if its a zero, we cant do nothing, sinkhole
#             else:
#                 result = dp(i+1)

#                 # if we are able to form a two_digit_required char, we do
#                 # if we are at least second to last(we can grab two)
#                 if i <= len(s)-2 and int(s[i:i+2]) <= 26:
#                     result += dp(i+2)
#                 return result
#         return dp(0)

# for bottom up, we can reuse the same definition of dp or change it to make iteration easier
# im gonna keep the same definition since it doesnt really make it harder
# dp(i) => number of ways we can decode s[i:]
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1)
        dp[len(s)] = 1

        for i in range(len(dp)-2, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i+1]
                if i <= len(s)-2 and int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]
        print(dp)
        return dp[0]










