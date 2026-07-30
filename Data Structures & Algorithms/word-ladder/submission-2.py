class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
            word_set = set(wordList)
    
            if endWord not in word_set:
                return 0
            
            n_iterations = 1
            current = [beginWord]
            
            while current:
                next_iteration = []
                for word in current:
                    if word == endWord:
                        return n_iterations
                    
                    for i in range(len(word)):
                        for char in 'abcdefghijklmnopqrstuvwxyz':
                            if char != word[i]:
                                new_word = word[:i] + char + word[i+1:]
                                
                                if new_word in word_set:
                                    next_iteration.append(new_word)
                                    word_set.discard(new_word)
                current = next_iteration
                n_iterations += 1
            return 0