class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        character_count = {}
        max_count = 0
        result = 0
        i = 0

        for j, c in enumerate(s):
            character_count[c] = character_count.get(c, 0) + 1
            max_count = max(max_count, character_count[c])

            while j-i+1 - max_count > k:
                character_count[s[i]] -= 1
                i += 1
            
            result = max(result, j-i+1)
        return result
        


        # length_of_window = count_of_max_repeating_character - 