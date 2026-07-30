class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # The problem states endWord MUST be in the wordList originally
        if endWord not in wordList:
            return 0
        
        word_length = len(beginWord)
        
        graph = collections.defaultdict(list)

        for word in wordList:
            for i in range(word_length):
                pattern = word[:i] + "*" + word[i+1:]
                graph[pattern].append(word)

        n_iterations = 1
        current = [beginWord]
        visited = set([beginWord])

        while current:
            next_iteration = []
            for current_word in current:
                if current_word == endWord:
                    return n_iterations
                for i in range(word_length):
                    pattern = current_word[:i] + "*" + current_word[i+1:]
                    for neighbor in graph[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            next_iteration.append(neighbor)
                    graph[pattern] = []
            n_iterations += 1
            current = next_iteration
        return 0
