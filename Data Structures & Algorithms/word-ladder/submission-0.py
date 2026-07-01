class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)

        if endWord not in wordList:
            return 0

        queue = collections.deque([(1, beginWord)])

        def is_path(word1: str, word2: str) -> bool:
            differed = False
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    if not differed:
                        differed = True
                    else:
                        return False
            return differed
        
        while queue:
            n_words, current = queue.popleft()

            if current == endWord:
                return n_words
            
            to_remove = []
            for neighbor in word_set:
                if is_path(current, neighbor):
                    to_remove.append(neighbor)
                    queue.append((n_words + 1, neighbor))
            
            for element in to_remove:
                word_set.discard(element)
        return 0