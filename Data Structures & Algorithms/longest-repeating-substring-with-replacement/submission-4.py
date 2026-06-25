class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        d = defaultdict(int)
        max_frequency = 0
        i = 0
        for j, character in enumerate(s):
            d[character] += 1
            max_frequency = max(max_frequency, d[character])

            while j-i+1 - max_frequency > k:
                d[s[i]] -= 1
                i += 1
            result = max(result, j-i+1)
        return result



