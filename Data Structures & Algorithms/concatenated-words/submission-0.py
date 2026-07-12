import functools

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words_set = set(words)
        result = []

        @functools.cache
        def helper(word: str) -> bool:
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in words_set and (suffix in words_set or helper(suffix)):
                    return True
            return False
        
        for word in words:
            if helper(word):
                result.append(word)
        return result


