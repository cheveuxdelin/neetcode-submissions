class Node:
    def __init__(self):
        self.is_word = False
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
        current.is_word = True

    def search(self, word: str) -> bool:
        def helper(current, i):
            if i == len(word):
                return current.is_word
            if word[i] == ".":
                return any(helper(current.children[child], i+1) for child in current.children)
            if word[i] in current.children:
                return helper(current.children[word[i]], i+1)
            return False
        
        return helper(self.root, 0)