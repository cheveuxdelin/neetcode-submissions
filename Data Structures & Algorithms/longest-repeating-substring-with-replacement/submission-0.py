
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d: dict[str, int] = {}
        longest_window = 0
        i = 0
        for j, c in enumerate(s):
            d[c] = d.get(c, 0) + 1
            
            count_of_most_repeated_character = max(d.values())
            
            while j - i + 1 - count_of_most_repeated_character > k:
                d[s[i]] -= 1
                if d[s[i]] == 0:
                    d.pop(s[i])
                i += 1
            longest_window = max(longest_window, j - i + 1)
        return longest_window