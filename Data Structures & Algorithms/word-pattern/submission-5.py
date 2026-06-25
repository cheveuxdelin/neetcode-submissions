class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        used_words = set()
        d = {}

        if len(words) != len(pattern):
            return False

        for i, p in enumerate(pattern):
            if p not in d:
                if words[i] in used_words:
                    return False
                d[p] = words[i]
                used_words.add(words[i])
            elif d[p] != words[i]:
                return False
        return True