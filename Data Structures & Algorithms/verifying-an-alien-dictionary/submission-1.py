class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {c: i for i, c in enumerate(order)}

        last = ""

        for word in words:
            i = 0
            while i < len(last) and i < len(word):
                if d[last[i]] < d[word[i]]:
                    break
                elif d[last[i]] > d[word[i]]:
                    return False
                i += 1
            else:
                if len(last) > len(word):
                    return False
            last = word
        return True