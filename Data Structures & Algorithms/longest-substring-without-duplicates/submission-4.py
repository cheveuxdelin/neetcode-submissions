class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        character_set = set()
        result = 0

        for character in s:
            while character in character_set:
                character_set.discard(s[i])
                i += 1
            character_set.add(character)
            result = max(result, len(character_set))
        return result