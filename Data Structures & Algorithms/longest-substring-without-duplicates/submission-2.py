class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        character_set = set()
        rtn = 0
        for j, c in enumerate(s):
            while c in character_set:
                character_set.discard(s[i])
                i += 1
            character_set.add(c)
            rtn = max(rtn, j-i+1)
        return rtn